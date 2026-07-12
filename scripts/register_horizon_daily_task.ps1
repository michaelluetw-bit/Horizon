param(
    [switch]$IncludeLogonTrigger
)

$ErrorActionPreference = "Stop"
$TaskName = "Horizon Daily Sync Publish"
$ProjectRoot = "C:\Users\micha\Documents\2026_agent\Horizon"
$ScriptPath = Join-Path $ProjectRoot "scripts\sync_latest.ps1"

if (-not (Test-Path -LiteralPath $ScriptPath)) {
    throw "Sync script not found: $ScriptPath"
}

$identity = [System.Security.Principal.WindowsIdentity]::GetCurrent()
$userSid = $identity.User.Value
$author = [System.Security.SecurityElement]::Escape($identity.Name)
$escapedScriptPath = [System.Security.SecurityElement]::Escape($ScriptPath)
$escapedProjectRoot = [System.Security.SecurityElement]::Escape($ProjectRoot)
$startBoundary = "{0}T09:00:00" -f ([DateTime]::Today.ToString("yyyy-MM-dd"))
$logonTrigger = ""
if ($IncludeLogonTrigger) {
    $logonTrigger = @"
    <LogonTrigger>
      <Enabled>true</Enabled>
      <UserId>$userSid</UserId>
    </LogonTrigger>
"@
}

$taskXml = @"
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Author>$author</Author>
    <Description>Pull the canonical Horizon report and publish it to the AI Executive Dashboard vault.</Description>
  </RegistrationInfo>
  <Triggers>
    <CalendarTrigger>
      <StartBoundary>$startBoundary</StartBoundary>
      <Enabled>true</Enabled>
      <ScheduleByDay><DaysInterval>1</DaysInterval></ScheduleByDay>
    </CalendarTrigger>
$logonTrigger
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>$userSid</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RestartOnFailure>
      <Interval>PT10M</Interval>
      <Count>3</Count>
    </RestartOnFailure>
    <ExecutionTimeLimit>PT1H</ExecutionTimeLimit>
    <Enabled>true</Enabled>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>powershell.exe</Command>
      <Arguments>-NoProfile -ExecutionPolicy Bypass -File &quot;$escapedScriptPath&quot;</Arguments>
      <WorkingDirectory>$escapedProjectRoot</WorkingDirectory>
    </Exec>
  </Actions>
</Task>
"@

$temporaryXml = [System.IO.Path]::GetTempFileName()
try {
    [System.IO.File]::WriteAllText($temporaryXml, $taskXml, [System.Text.Encoding]::Unicode)
    & schtasks.exe /Create /TN $TaskName /XML $temporaryXml /F | Write-Output
    if ($LASTEXITCODE -ne 0) {
        throw "Task Scheduler registration failed with exit code $LASTEXITCODE."
    }
} finally {
    Remove-Item -LiteralPath $temporaryXml -Force -ErrorAction SilentlyContinue
}

Write-Output "STATUS=SUCCESS"
Write-Output "TASK_NAME=$TaskName"
