# CCU Assistant

你的中正大學 AI 助手。它會操作 Chrome 幫你從 eCourse2、iCCU 教務系統抓資料回來，查課程、下載教材、整理作業截止日期、看成績都行。

An AI assistant for CCU students. It drives Chrome to fetch data from eCourse2 (Moodle) and iCCU — courses, materials, deadlines, grades, whatever you need.

## 能做什麼

- 同步 eCourse2 上的課程、公告、作業、成績
- 下載講義和簡報
- 從 iCCU 抓課表、歷年成績
- 查 eCourse2 通知
- 查開課資料 / 課程大綱
- 請假
- 整理完的資料可以做成一頁式網頁

## 安裝（三步）

### 1. 裝 Claude Code

需要 [Node.js](https://nodejs.org/) v20+

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. 設定 Chrome 連線

在 Claude Code 裡跑：

```
claude mcp add chrome-devtools -- npx chrome-devtools-mcp@latest --browserUrl=http://127.0.0.1:9222
```

如果上面指令報錯，手動編輯 `~/.claude.json`，在 `mcpServers` 裡加入：

```json
"chrome-devtools": {
  "command": "npx",
  "args": [
    "chrome-devtools-mcp@latest",
    "--browserUrl=http://127.0.0.1:9222"
  ]
}
```

### 3. 裝 Skill

```bash
git clone https://github.com/febsi29/ccu.git ~/.claude/skills/ccu
```

完成！

## 使用方式

每次用就兩步：

### Step 1：開 Chrome

雙擊 repo 裡附的啟動腳本：

- **Windows**：`start-chrome.bat`
- **Mac**：`start-chrome.sh`

Chrome 會開啟並跳到 eCourse2。**第一次需要手動登入，之後都會記住。**

<details>
<summary>沒有腳本？手動開也行</summary>

先關掉所有 Chrome，然後開終端機跑：

Windows:
```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="%HOMEPATH%\.chrome-ccu-profile" https://ecourse2.ccu.edu.tw
```

Mac:
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --remote-debugging-port=9222 --user-data-dir="$HOME/.chrome-ccu-profile" https://ecourse2.ccu.edu.tw &
```

</details>

### Step 2：開 Claude Code

```bash
claude
```

然後輸入：

```
/ccu
```

它會列出能做的事讓你選。也可以直接講：

```
/ccu 這週有什麼作業？
/ccu 幫我下載所有課程教材
/ccu 整理課表和近期作業
/ccu 幫我看成績
/ccu 請假
```

## 為什麼要先開 Chrome？

CCU 的網站有 Cloudflare 防護，會擋掉自動化工具開的瀏覽器。用你自己開的 Chrome 就不會被擋，而且登入狀態會保留。

## ⚠️ 注意事項

- 使用前請先關掉其他 Chrome 視窗，再用腳本開
- 部分系統（如 iCCU）可能限校內網路，請確認有連上中正校園網路或 VPN
- 同步多門課程時需要逐頁瀏覽，8 門課完整同步約需 3-5 分鐘
- eCourse2 的 Moodle API 已被學校關閉，所有資料透過瀏覽器頁面解析

## 安全

- 帳密只用來當場填入登入表單，不存
- 所有資料都在你電腦上
- Chrome 的 debug port 只開在本機（127.0.0.1），外部無法連入

## 致謝

本專案架構參考自 [YouMingYeh/ntu](https://github.com/YouMingYeh/ntu)（NTU Assistant），感謝原作者的開源貢獻。

## License

MIT
