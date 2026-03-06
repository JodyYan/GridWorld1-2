# 開發紀錄 (Development Log)

## 2026-03-07
- **00:32**: 初始化開發紀錄檔案 (`log.md`)。接下來的開發對話將會記錄在此檔案中。
- **00:38**: 開始實作強化學習環境與演算法 (`main.py`)。思考：需要建立 `GridWorld` 模型（定義 7x7 網格、終點、行動、轉移、獎勵）。定義 `ValueIterationSolver` 實作 Value Iteration。定義 `Visualizer` 以 matplotlib 和 seaborn 繪製結果並存檔。同時撰寫 `requirements.txt`。
- **00:40**: 完成腳本編寫。準備在本地端進行測試，執行 `main.py` 並查看是否能成功產出 `gridworld_result.png`。
- **00:45**: 在測試過程中發現 `seaborn` 的 colormap `white` 會引發錯誤，且 matplotlib 預設 backend 可能在無介面環境導致卡住。修正了 `cmap=ListedColormap(['white'])` 並設定 `matplotlib.use('Agg')`後測試成功，`gridworld_result.png` 順利產出。
- **00:46**: 建立 `index.html`，完成 Demo Page 基本架構，將測試圖檔嵌入。
- **00:47**: 準備進行 GitHub 版本控制與部署，將執行 `git init`, `git add .`, 和 `git commit`。
- **00:50**: 成功在本地端初始化 Git 檔案庫並提交所有檔案（`main.py`, `log.md`, `index.html`, `requirements.txt`, `gridworld_result.png`）。但由於環境中缺少 GitHub CLI (`gh`)，無法自動建立遠端儲存庫。準備請使用者提供 Remote URL 或是手動在 GitHub 建立儲存庫。
- **00:44**: 使用者希望先查看本地端的 Demo 網站。準備啟動 Python 內建的 HTTP 伺服器來提供預覽。
- **00:54**: 收到追加任務，要求建立純前端（JavaScript + CSS）的互動式 Demo 網頁，覆蓋原先的靜態 `index.html`，並嚴格保持 `main.py` 及原圖檔不變。開始撰寫網頁。
- **00:55**: 完成前端互動版 `index.html`，實作了網格渲染、Value Iteration 演算法 (JS)、以及單步執行/自動收斂/重置等控制按鈕。現在進行 Git 追蹤與提交。
- **01:05**: 撰寫 `README.md` 說明文件，並準備將專案推送到使用者的 GitHub Repository (`https://github.com/JodyYan/GridWorld1-2.git`) 的 `main` 與 `gh-pages` 分支。
- **01:06**: 成功將專案推送至 GitHub 遠端儲存庫的 `main` 分支，並同步推送至 `gh-pages` 分支。任務圓滿完成。
- **01:07**: 嘗試使用內建瀏覽器代理工具自動開啟 GitHub 設定頁面啟用 GitHub Pages，但遭遇瀏覽器環境限制無法順利開啟目標網頁，需要請使用者手動點擊啟用。
