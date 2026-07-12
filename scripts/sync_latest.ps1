param(
    [string]$ProjectRoot = "C:\Users\micha\Documents\2026_agent\Horizon",
    [string]$TargetDir = "C:\Users\micha\Documents\2026_agent\download\knowledge\19_codex\AI Executive Dashboard\01_Horizon",
    [string]$DashboardBaseUrl = "http://127.0.0.1:5173",
    [string]$ArtifactDate = ""
)

$ErrorActionPreference = "Stop"
$LogPath = Join-Path $env:TEMP "horizon-daily-publish.log"
$MutexName = "Global\HorizonDailyCloudToLocalPublish"
$ExitCode = 0
$Mutex = $null
$MutexAcquired = $false

function Write-StructuredLog {
    param([string]$Message)
    $line = "{0} {1}" -f ([DateTimeOffset]::Now.ToString("o")), $Message
    Write-Output $Message
    Add-Content -LiteralPath $LogPath -Value $line -Encoding UTF8
}

function Stop-Pipeline {
    param([string]$Status, [int]$Code, [string]$Detail)
    Write-StructuredLog "STATUS=$Status"
    if ($Detail) { Write-StructuredLog "DETAIL=$Detail" }
    $exception = [System.Exception]::new($Status)
    $exception.Data["PipelineStop"] = $true
    $exception.Data["ExitCode"] = $Code
    throw $exception
}

try {
    $Mutex = [System.Threading.Mutex]::new($false, $MutexName)
    $MutexAcquired = $Mutex.WaitOne(0)
    if (-not $MutexAcquired) {
        Stop-Pipeline "PUBLISH_FAILED" 30 "Another Horizon publish process is already running."
    }

    if (-not (Test-Path -LiteralPath (Join-Path $ProjectRoot ".git"))) {
        Stop-Pipeline "INVALID_REPOSITORY" 10 "Horizon repository not found: $ProjectRoot"
    }

    $branch = (& git -C $ProjectRoot branch --show-current 2>&1 | Out-String).Trim()
    if ($LASTEXITCODE -ne 0 -or $branch -ne "main") {
        Stop-Pipeline "WRONG_BRANCH" 11 "Expected main, found '$branch'."
    }

    $workingTree = (& git -C $ProjectRoot status --porcelain 2>&1 | Out-String).Trim()
    if ($LASTEXITCODE -ne 0) {
        Stop-Pipeline "INVALID_REPOSITORY" 10 $workingTree
    }
    if ($workingTree) {
        Stop-Pipeline "DIRTY_WORKTREE" 12 "Local changes must be committed or stashed manually."
    }

    $pullOutput = (& git -C $ProjectRoot pull --ff-only origin main 2>&1 | Out-String).Trim()
    if ($LASTEXITCODE -ne 0) {
        Stop-Pipeline "PULL_FAILED" 13 $pullOutput
    }
    Write-StructuredLog "LOCAL_PULL_SUCCESS=true"

    if (-not $ArtifactDate) {
        $taipeiZone = [TimeZoneInfo]::FindSystemTimeZoneById("Taipei Standard Time")
        $ArtifactDate = [TimeZoneInfo]::ConvertTimeFromUtc([DateTime]::UtcNow, $taipeiZone).ToString("yyyy-MM-dd")
    }
    Write-StructuredLog "SOURCE_TIMEZONE=Asia/Taipei"
    Write-StructuredLog "ARTIFACT_DATE=$ArtifactDate"

    $sourceDir = Join-Path $ProjectRoot "data\summaries"
    $expectedName = "horizon-$ArtifactDate-zh.md"
    $expectedSource = Join-Path $sourceDir $expectedName
    if (-not (Test-Path -LiteralPath $expectedSource -PathType Leaf)) {
        $matches = @(Get-ChildItem -LiteralPath $sourceDir -Filter "horizon-$ArtifactDate-*.md" -File -ErrorAction SilentlyContinue)
        if ($matches.Count -eq 0) {
            Stop-Pipeline "SOURCE_NOT_FOUND" 20 "No Horizon source for $ArtifactDate."
        }
        Stop-Pipeline "SOURCE_INVALID" 22 "Expected $expectedName, found $($matches.Name -join ', ')."
    }
    Write-StructuredLog "SOURCE_MATCH_COUNT=1"

    $python = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
    $publisher = Join-Path $ProjectRoot "scripts\publish_horizon.py"
    if (-not (Test-Path -LiteralPath $python) -or -not (Test-Path -LiteralPath $publisher)) {
        Stop-Pipeline "PUBLISH_FAILED" 30 "Publisher runtime is unavailable."
    }

    $publishOutput = (& $python $publisher --date $ArtifactDate --source-dir $sourceDir --target-dir $TargetDir 2>&1 | Out-String).Trim()
    $publishCode = $LASTEXITCODE
    Write-StructuredLog $publishOutput
    if ($publishCode -ne 0) {
        $knownStatus = [regex]::Match($publishOutput, "STATUS=([A-Z_]+)").Groups[1].Value
        if ($knownStatus) { Stop-Pipeline $knownStatus $publishCode "Publisher rejected the artifact." }
        Stop-Pipeline "PUBLISH_FAILED" 30 $publishOutput
    }
    $publishStatus = [regex]::Match($publishOutput, "STATUS=(SUCCESS|ALREADY_PUBLISHED)").Groups[1].Value
    if (-not $publishStatus) {
        Stop-Pipeline "PUBLISH_FAILED" 30 "Publisher returned no recognized status."
    }
    Write-StructuredLog "PUBLISH_SUCCESS=true"

    try {
        $payload = Invoke-RestMethod -Uri "$DashboardBaseUrl/api/artifacts" -TimeoutSec 5
    } catch {
        Stop-Pipeline "PUBLISH_SUCCESS_DASHBOARD_UNAVAILABLE" 40 $_.Exception.Message
    }

    $expectedRelativePath = "01_Horizon\$ArtifactDate-horizon.md"
    $artifact = $payload.artifacts | Where-Object {
        $_.relativePath -eq $expectedRelativePath -and
        $_.date -eq $ArtifactDate -and
        $_.module -eq "horizon" -and
        $_.agent -eq "Horizon" -and
        $_.status -eq "completed" -and
        $_.source -eq "data/summaries/$expectedName"
    } | Select-Object -First 1
    if (-not $artifact) {
        Stop-Pipeline "DASHBOARD_VALIDATION_FAILED" 41 "Dashboard did not return the canonical published artifact."
    }

    Write-StructuredLog "DASHBOARD_VERIFY_SUCCESS=true"
    Write-StructuredLog "STATUS=$publishStatus"
    $ExitCode = 0
} catch {
    if ($_.Exception.Data["PipelineStop"]) {
        $ExitCode = [int]$_.Exception.Data["ExitCode"]
    } else {
        Write-StructuredLog "STATUS=PUBLISH_FAILED"
        Write-StructuredLog "DETAIL=$($_.Exception.Message)"
        $ExitCode = 30
    }
} finally {
    if ($MutexAcquired -and $Mutex) { $Mutex.ReleaseMutex() }
    if ($Mutex) { $Mutex.Dispose() }
}

exit $ExitCode
