# Horizon Local Sync Script
# 配合 Windows 工作排程器於開機或登入時自動執行

$ProjectRoot = "C:\Users\micha\Documents\2026_agent\Horizon"
Set-Location $ProjectRoot

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Horizon: 正在從 GitHub 雲端同步最新快報..." -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 執行 Git Pull
$pullResult = git pull origin main 2>&1

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n[✅ 成功] 快報同步完成！您的本機資料夾已是最新狀態。" -ForegroundColor Green
} else {
    Write-Host "`n[⚠️ 警告] Git 同步遇到問題，請手動確認網路連線或憑證設定。" -ForegroundColor Yellow
    Write-Host "錯誤詳情: $pullResult" -ForegroundColor Red
}

# 暫停 3 秒讓使用者有時間看輸出
Start-Sleep -Seconds 3
