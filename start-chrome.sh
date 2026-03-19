#!/bin/bash
echo "正在啟動 Chrome（CCU Assistant 模式）..."
echo "請在 Chrome 登入 eCourse2 後，再開你的 AI agent 輸入 /ccu"
echo ""
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/.chrome-ccu-profile" \
  https://ecourse2.ccu.edu.tw &
