<div align="center">

# 🎓 CCU Assistant

**讓 AI 幫你處理中正大學的大小事**

操作你的 Chrome → 登入 eCourse2、iCCU → 自動抓資料 → 整理好給你

支援所有 MCP 相容的 AI agent（Claude Code、Cursor、Windsurf、Codex 等）

</div>

---

## 這是什麼？

一個給 AI coding agent 用的 skill，專門服務中正大學學生。它會像你一樣操作瀏覽器 —— 點進 eCourse2 看公告、翻作業截止日、下載講義 —— 只是比你快，而且會自動整理。

> ⚡ 因為 CCU 網站有 Cloudflare 防護，AI 直接開的瀏覽器會被擋。所以需要你**先手動開 Chrome**，AI 再接手操作。第一次登入後 Chrome 會記住，之後就是秒開。

---

## 能幫你做什麼

| 功能 | 來源 |
|------|------|
| 同步課程公告、作業、教材、成績 | eCourse2 |
| 下載講義和簡報 | eCourse2 |
| 查近期作業和截止日期 | eCourse2 行事曆 |
| 抓課表、歷年成績 | iCCU |
| 查 eCourse2 通知 | eCourse2 |
| 查開課資料 / 課程大綱 | eCourse2 / iCCU |
| 請假 | 學生請假系統 |
| 在學證明 | 學籍系統 |
| 做成一頁式課程總覽網頁 | 自動生成 |

---

## 怎麼用

```
Step 1 → 雙擊 start-chrome.bat（Windows）或 start-chrome.sh（Mac）
Step 2 → 開你的 AI agent，輸入 /ccu
```

就這樣。第一次會需要在 Chrome 登入 eCourse2，你可以自己登，或讓 AI 幫你填帳密。登一次就夠了，CCU 各系統共用 SSO。

想跳過選單直接做事也行：

```
/ccu 這週有什麼作業？
/ccu 幫我下載所有課程教材
/ccu 整理課表和近期作業
/ccu 幫我看成績
/ccu 請假
```

---

## 安裝

### 你需要先有

- [Node.js](https://nodejs.org/) v20 以上
- 一個支援 MCP 的 AI agent（[Claude Code](https://docs.anthropic.com/en/docs/claude-code)、Cursor、Windsurf、Codex 等）
- Chrome 瀏覽器

### 三步搞定

**① 設定 Chrome 連線**

在你的 AI agent 的 MCP 設定裡加入：

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "chrome-devtools-mcp@latest",
        "--browserUrl=http://127.0.0.1:9222"
      ]
    }
  }
}
```

<details>
<summary>各 agent 的設定檔位置</summary>

- **Claude Code**：`~/.claude.json` 裡的 `mcpServers` 欄位
- **Cursor**：Settings → MCP → 加入上面的設定
- **Windsurf**：`~/.windsurf/mcp.json`
- **其他**：參考你的 agent 的 MCP 設定文件

</details>

**② 裝 Skill**

```bash
git clone https://github.com/febsi29/ccu.git ~/.claude/skills/ccu
```

過程有東西跳出來？**全部按 Enter。**

**③ 開 Chrome**

雙擊 repo 裡的 `start-chrome.bat`（Windows）或 `start-chrome.sh`（Mac）。

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

✅ 搞定。開你的 AI agent，輸入 `/ccu`。

---

## 為什麼要先開 Chrome？

CCU 的 eCourse2 和 iCCU 前面架了 Cloudflare 防護。當 AI 工具自動開瀏覽器時，Cloudflare 會偵測到自動化行為並擋下來 —— 就算你手動去點驗證也過不了。

解法很簡單：**你自己開 Chrome，AI 再連上來操作。** `start-chrome.bat` 就是做這件事，它用一行指令開 Chrome 並打開 debug port，讓你的 AI agent 可以接手。對 Cloudflare 來說，這就是一個普通的 Chrome，不會被擋。

登入狀態存在 `.chrome-ccu-profile` 資料夾裡，下次開還在。

---

## 注意事項

- **開 Chrome 前請先關掉其他 Chrome 視窗**，避免 port 衝突
- 部分系統（如 iCCU）可能限校內網路，需要連中正校園網路或 VPN
- 同步多門課程需逐頁瀏覽，8 門課約 3-5 分鐘
- eCourse2 的 Moodle API 被學校關掉了，所有資料靠瀏覽器頁面解析

---

## 安全性

- 🔒 帳密只用來填登入表單，填完即棄，不存任何地方
- 💻 所有抓到的資料都只在你的電腦上
- 🌐 Chrome debug port 只開在 `127.0.0.1`，外部無法連入

---

## 致謝

架構參考自 [YouMingYeh/ntu](https://github.com/YouMingYeh/ntu)（NTU Assistant），感謝原作者的開源貢獻。

## License

MIT
