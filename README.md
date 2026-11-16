# 拾光知識庫

一個可以持續新增獨立文章的繁體中文知識收藏網站。

- [公開網站](https://ukchen0107-cpu.github.io/my-website/)
- [第一篇文章：番茄鐘工作法](https://ukchen0107-cpu.github.io/my-website/pages/pomodoro.html)

## 如何透過 AI 新增文章
在能讀寫此 GitHub 儲存庫的 AI 程式工具（例如具備 GitHub 權限的編碼代理）中，貼上：

> 請先閱讀 AGENTS.md，依照規則新增一篇獨立文章。主題：費曼學習法。分類：學習方法。請自行整理適合初學者的介紹、步驟與實際例子；建立 pages/ 下的 HTML 檔案，更新 data/pages.json，保留既有文章，執行 python3 scripts/validate.py，最後告訴我修改了哪些檔案及驗證結果。

AI 工具必須有儲存庫寫入權限，才能直接提交；沒有權限時只能產出檔案供人工提交。AGENTS.md 本身不會自動執行 AI。

## 專案架構
- `AGENTS.md`：AI 員工手冊與新增文章規範
- `index.html`：首頁、搜尋與分類
- `data/pages.json`：首頁文章索引
- `pages/`：獨立 HTML 文章
- `scripts/validate.py`：索引與頁面檢查程式
- `.github/workflows/validate.yml`：提交與 PR 時自動驗證

目前首頁樣式與 JavaScript 內嵌在 index.html；獨立文章也使用內嵌樣式，尚未抽出共用 style.css 或 script.js。

## 更新與部署
1. 新增 pages/xxx.html。
2. 在 data/pages.json 新增包含 title、category、summary、date、url 的物件，URL 使用 pages/xxx.html。
3. 執行 `python3 scripts/validate.py`，確認沒有錯誤。
4. 將變更提交到 main。GitHub Actions 執行索引驗證；GitHub Pages 另外部署網站。
5. 部署後開啟公開首頁，檢查文章卡片、搜尋、分類與文章連結。

注意：自動驗證僅檢查索引結構與文章檔案，不等於瀏覽器視覺測試，也不保證 Pages 已成功部署。
