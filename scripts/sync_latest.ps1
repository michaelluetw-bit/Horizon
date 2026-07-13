param(
    [string]$ProjectRoot = "C:\Users\micha\Documents\2026_agent\Horizon",
    [string]$TargetDir = "C:\Users\micha\Documents\2026_agent\download\knowledge\19_codex\AI Executive Dashboard\01_Horizon",
    [string]$DashboardBaseUrl = "http://127.0.0.1:5173",
    [string]$ArtifactDate = "",
    [string]$PythonExecutable = ""
)

$ErrorActionPreference = "Stop"
$LogPath = Join-Path $env:TEMP "horizon-daily-publish.log"
$MutexName = "Global\HorizonDailyCloudToLocalPublish"
$ExitCode = 0
$Mutex = $null
$MutexAcquired = $false
$TemporarySource = $null

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

function Invoke-NativeText {
    param(
        [string]$FilePath,
        [string[]]$CommandArguments
    )

    $previousErrorActionPreference = $ErrorActionPreference
    try {
        $ErrorActionPreference = "Continue"
        $output = (& $FilePath @CommandArguments 2>&1 | Out-String).TrimEnd()
        $exitCode = $LASTEXITCODE
    } finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }

    return [pscustomobject]@{
        ExitCode = $exitCode
        Output = $output
    }
}

function Invoke-GitText {
    param([string[]]$GitArguments)
    return Invoke-NativeText -FilePath "git.exe" -CommandArguments $GitArguments
}

function Export-GitBlob {
    param(
        [string]$ObjectName,
        [string]$Destination
    )

    $startInfo = New-Object System.Diagnostics.ProcessStartInfo
    $startInfo.FileName = "git.exe"
    $escapedRoot = $ProjectRoot.Replace('"', '\"')
    $escapedObject = $ObjectName.Replace('"', '\"')
    $startInfo.Arguments = ('-C "{0}" cat-file blob "{1}"' -f $escapedRoot, $escapedObject)
    $startInfo.UseShellExecute = $false
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $true
    $startInfo.CreateNoWindow = $true

    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $startInfo
    [void]$process.Start()
    $errorTask = $process.StandardError.ReadToEndAsync()
    $destinationStream = [System.IO.File]::Open(
        $Destination,
        [System.IO.FileMode]::CreateNew,
        [System.IO.FileAccess]::Write,
        [System.IO.FileShare]::None
    )
    try {
        $copyTask = $process.StandardOutput.BaseStream.CopyToAsync($destinationStream)
        $process.WaitForExit()
        $copyTask.GetAwaiter().GetResult()
        $errorOutput = $errorTask.GetAwaiter().GetResult()
    } finally {
        $destinationStream.Dispose()
    }

    return [pscustomobject]@{
        ExitCode = $process.ExitCode
        ErrorOutput = $errorOutput.Trim()
    }
}

function Test-OnlyGeneratedSummaryDirty {
    param(
        [string]$Porcelain,
        [string]$AllowedPath
    )

    $entries = @($Porcelain -split "`r?`n" | Where-Object { $_.Trim() })
    foreach ($entry in $entries) {
        if ($entry.Length -lt 4 -or $entry -match " -> " -or $entry.Substring(2) -ne " $AllowedPath") {
            return $false
        }
    }
    return $true
}

try {
    $Mutex = [System.Threading.Mutex]::new($false, $MutexName)
    $MutexAcquired = $Mutex.WaitOne(0)
    if (-not $MutexAcquired) {
        Stop-Pipeline "VAULT_PUBLISH_FAILED" 30 "Another Horizon publish process is already running."
    }

    if (-not (Test-Path -LiteralPath (Join-Path $ProjectRoot ".git"))) {
        Stop-Pipeline "INVALID_REPOSITORY" 10 "Horizon repository not found: $ProjectRoot"
    }

    $branchResult = Invoke-GitText -GitArguments @("-C", $ProjectRoot, "branch", "--show-current")
    if ($branchResult.ExitCode -ne 0 -or $branchResult.Output -ne "main") {
        Stop-Pipeline "WRONG_BRANCH" 11 "Expected main, found '$($branchResult.Output)'."
    }

    if (-not $ArtifactDate) {
        $taipeiZone = [TimeZoneInfo]::FindSystemTimeZoneById("Taipei Standard Time")
        $ArtifactDate = [TimeZoneInfo]::ConvertTimeFromUtc([DateTime]::UtcNow, $taipeiZone).ToString("yyyy-MM-dd")
    }
    $expectedName = "horizon-$ArtifactDate-zh.md"
    $sourceRef = "data/summaries/$expectedName"

    $fetchResult = Invoke-GitText -GitArguments @("-C", $ProjectRoot, "fetch", "origin", "main")
    if ($fetchResult.ExitCode -ne 0) {
        Stop-Pipeline "ORIGIN_FETCH_FAILED" 13 $fetchResult.Output
    }
    Write-StructuredLog "ORIGIN_FETCH_SUCCESS=true"
    Write-StructuredLog "SOURCE_TIMEZONE=Asia/Taipei"
    Write-StructuredLog "ARTIFACT_DATE=$ArtifactDate"

    $workingTreeResult = Invoke-GitText -GitArguments @("-C", $ProjectRoot, "status", "--porcelain")
    if ($workingTreeResult.ExitCode -ne 0) {
        Stop-Pipeline "INVALID_REPOSITORY" 10 $workingTreeResult.Output
    }
    if (-not (Test-OnlyGeneratedSummaryDirty -Porcelain $workingTreeResult.Output -AllowedPath $sourceRef)) {
        Stop-Pipeline "DIRTY_CODE_WORKTREE" 12 "Only the current generated summary may be dirty."
    }
    Write-StructuredLog "WORKTREE_GATE_SUCCESS=true"

    $originObject = "origin/main:$sourceRef"
    $objectType = Invoke-GitText -GitArguments @("-C", $ProjectRoot, "cat-file", "-t", $originObject)
    if ($objectType.ExitCode -ne 0) {
        Stop-Pipeline "TODAY_OUTPUT_MISSING" 20 "No origin/main source for $ArtifactDate."
    }
    if ($objectType.Output -ne "blob") {
        Stop-Pipeline "TODAY_OUTPUT_INVALID" 22 "Expected a blob at $sourceRef."
    }

    $TemporarySource = Join-Path ([System.IO.Path]::GetTempPath()) ("horizon-origin-" + [guid]::NewGuid().ToString("N") + ".md")
    try {
        $blobResult = Export-GitBlob -ObjectName $originObject -Destination $TemporarySource
    } catch {
        Stop-Pipeline "ORIGIN_BLOB_READ_FAILED" 23 $_.Exception.Message
    }
    if ($blobResult.ExitCode -ne 0) {
        Stop-Pipeline "ORIGIN_BLOB_READ_FAILED" 23 $blobResult.ErrorOutput
    }
    Write-StructuredLog "ORIGIN_BLOB_READ_SUCCESS=true"

    $python = if ($PythonExecutable) { $PythonExecutable } else { Join-Path $ProjectRoot ".venv\Scripts\python.exe" }
    $publisher = Join-Path $ProjectRoot "scripts\publish_horizon.py"
    if (-not (Test-Path -LiteralPath $python) -or -not (Test-Path -LiteralPath $publisher)) {
        Stop-Pipeline "VAULT_PUBLISH_FAILED" 30 "Publisher runtime is unavailable."
    }

    $publishResult = Invoke-NativeText -FilePath $python -CommandArguments @(
        $publisher,
        "--date", $ArtifactDate,
        "--source-file", $TemporarySource,
        "--source-ref", $sourceRef,
        "--target-dir", $TargetDir
    )
    if ($publishResult.Output) { Write-StructuredLog $publishResult.Output }
    if ($publishResult.ExitCode -ne 0) {
        $knownStatus = [regex]::Match($publishResult.Output, "STATUS=([A-Z_]+)").Groups[1].Value
        if ($knownStatus -eq "SOURCE_INVALID") {
            Stop-Pipeline "TODAY_OUTPUT_INVALID" 22 "Publisher rejected the origin blob."
        }
        Stop-Pipeline "VAULT_PUBLISH_FAILED" 30 $publishResult.Output
    }
    $publishStatus = [regex]::Match($publishResult.Output, "STATUS=(SUCCESS|ALREADY_PUBLISHED)").Groups[1].Value
    if (-not $publishStatus) {
        Stop-Pipeline "VAULT_PUBLISH_FAILED" 30 "Publisher returned no recognized status."
    }
    Write-StructuredLog "VAULT_PUBLISH_SUCCESS=true"

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
        $_.source -eq $sourceRef
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
        Write-StructuredLog "STATUS=VAULT_PUBLISH_FAILED"
        Write-StructuredLog "DETAIL=$($_.Exception.Message)"
        $ExitCode = 30
    }
} finally {
    if ($TemporarySource -and (Test-Path -LiteralPath $TemporarySource -PathType Leaf)) {
        Remove-Item -LiteralPath $TemporarySource -Force -ErrorAction SilentlyContinue
    }
    if ($MutexAcquired -and $Mutex) { $Mutex.ReleaseMutex() }
    if ($Mutex) { $Mutex.Dispose() }
}

exit $ExitCode
