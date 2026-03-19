@echo off
echo 正在啟動 Chrome（CCU Assistant 模式）...
echo 請在 Chrome 登入 eCourse2 後，再開你的 AI agent 輸入 /ccu
echo.
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="%HOMEPATH%\.chrome-ccu-profile" https://ecourse2.ccu.edu.tw
