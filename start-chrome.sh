#!/usr/bin/env bash
set -euo pipefail

case "$(uname -s)" in
  Darwin)
    chrome_exe="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    profile_dir="$HOME/Library/Application Support/CCUAssistant/ChromeProfile"
    ;;
  Linux)
    chrome_exe="$(command -v google-chrome || command -v google-chrome-stable || true)"
    profile_dir="${XDG_DATA_HOME:-$HOME/.local/share}/ccu-assistant/chrome-profile"
    ;;
  *)
    echo "[ERROR] 此腳本僅支援 macOS 與 Linux；Windows 請使用 start-chrome.bat。" >&2
    exit 1
    ;;
esac

if [[ -z "${chrome_exe}" || ! -x "${chrome_exe}" ]]; then
  echo "[ERROR] 找不到可執行的 Google Chrome。" >&2
  exit 1
fi

mkdir -p "${profile_dir}"

echo "正在啟動 Chrome（CCU Assistant 專用模式）..."
echo "請在 Chrome 內自行登入 eCourse2，再開啟 AI agent 輸入 /ccu。"

"${chrome_exe}" \
  --remote-debugging-address=127.0.0.1 \
  --remote-debugging-port=9222 \
  --user-data-dir="${profile_dir}" \
  https://ecourse2.ccu.edu.tw &
