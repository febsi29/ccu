# CCU Assistant

你的中正大學 AI 助手。它會操作 Chrome 幫你從 eCourse2、iCCU 教務系統抓資料回來，查課程、下載教材、整理作業截止日期、看成績都行。

An AI assistant for CCU students. It drives Chrome to fetch data from eCourse2 (Moodle) and iCCU — courses, materials, deadlines, grades, whatever you need.

## 能做什麼

- 同步 eCourse2 上的課程、公告、作業、成績
- 下載講義和簡報
- 從 iCCU 抓課表、歷年成績
- 查 eCourse2 通知（取代 email）
- 查開課資料
- 整理完的資料可以做成一頁式網頁

## 裝之前

1. [Node.js](https://nodejs.org/) v20+
2. 一個支援 [skills](https://skills.sh) 的 AI 工具（Claude Code、Codex、Cursor 都行）
3. 讓 AI 可以操作 Chrome：

```bash
claude mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```

用的時候它會自己開 Chrome，不用手動。

<details>
<summary>其他工具的設定</summary>

在 MCP 設定檔加：

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

</details>

## 安裝

```bash
npx skills add YOUR_GITHUB_USERNAME/ccu
```

過程中問的問題，**全部按 Enter** 就好。

更新：`npx skills update`

<details>
<summary>手動裝</summary>

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/ccu.git ~/.claude/skills/ccu
```

</details>

## 用法

輸入 `/ccu`，它會列出能做的事讓你選。也可以直接講：

```
/ccu
/ccu 幫我下載所有課程教材
/ccu 整理課表和近期作業
/ccu 這週有什麼作業？
/ccu 幫我看成績
/ccu Download all course materials
/ccu What's due this week?
```

第一次用會開 Chrome 處理登入。你可以給帳密讓它填，或自己在 Chrome 登好再告訴它。登一次就夠了，CCU 各系統共用 SSO。

## ⚠️ 注意事項

- 部分系統（如 iCCU 選課系統）可能限校內網路，請確認有連上中正校園網路或 VPN
- eCourse2 的 Moodle Web Service API 已被學校關閉，所有資料透過瀏覽器頁面解析抓取
- 同步多門課程時需要逐頁瀏覽，8 門課完整同步約需 2-5 分鐘

## 安全

帳密只用來當場填入登入表單，不存。資料都在你電腦上。

## 致謝

本專案架構參考自 [YouMingYeh/ntu](https://github.com/YouMingYeh/ntu)（NTU Assistant），感謝原作者的開源貢獻。

## License

MIT
