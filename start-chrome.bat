@echo off
setlocal

set "CHROME_EXE=%ProgramFiles%\Google\Chrome\Application\chrome.exe"
if not exist "%CHROME_EXE%" set "CHROME_EXE=%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
if not exist "%CHROME_EXE%" set "CHROME_EXE=%LocalAppData%\Google\Chrome\Application\chrome.exe"

if not exist "%CHROME_EXE%" (
  echo [ERROR] 找不到 Google Chrome，請先安裝 Chrome。
  exit /b 1
)

set "PROFILE_DIR=%LocalAppData%\CCUAssistant\ChromeProfile"

echo 正在啟動 Chrome（CCU Assistant 專用模式）...
echo 請在 Chrome 內自行登入 eCourse2，再開啟 AI agent 輸入 /ccu。
echo.

start "" "%CHROME_EXE%" ^
  --remote-debugging-address=127.0.0.1 ^
  --remote-debugging-port=9222 ^
  --user-data-dir="%PROFILE_DIR%" ^
  https://ecourse2.ccu.edu.tw

endlocal
