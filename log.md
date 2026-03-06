# 開發紀錄 (Development Log)

## 2026-03-07
- **00:32**: 初始化開發紀錄檔案 (`log.md`)。接下來的開發對話將會記錄在此檔案中。
- **00:38**: 開始實作強化學習環境與演算法 (`main.py`)。思考：需要建立 `GridWorld` 模型（定義 7x7 網格、終點、行動、轉移、獎勵）。定義 `ValueIterationSolver` 實作 Value Iteration。定義 `Visualizer` 以 matplotlib 和 seaborn 繪製結果並存檔。同時撰寫 `requirements.txt`。
- **00:40**: 完成腳本編寫。準備在本地端進行測試，執行 `main.py` 並查看是否能成功產出 `gridworld_result.png`。
- **00:45**: 在測試過程中發現 `seaborn` 的 colormap `white` 會引發錯誤，且 matplotlib 預設 backend 可能在無介面環境導致卡住。修正了 `cmap=ListedColormap(['white'])` 並設定 `matplotlib.use('Agg')`後測試成功，`gridworld_result.png` 順利產出。
- **00:46**: 建立 `index.html`，完成 Demo Page 基本架構，將測試圖檔嵌入。
- **00:47**: 準備進行 GitHub 版本控制與部署，將執行 `git init`, `git add .`, 和 `git commit`。
