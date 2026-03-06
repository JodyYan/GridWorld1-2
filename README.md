# GridWorld Value Iteration Demo

這是一個經典的 7x7 Gridworld 強化學習作業實作。專案包含了 Python 的演算法實作、圖形視覺化，以及一個以純前端技術 (JavaScript + HTML + CSS) 開發的互動式 Demo 網頁。

## 專案結構

- `main.py`: 高可維護性、基於物件導向 (OOP) 的 Python 腳本。實作了 `GridWorld` 環境、`ValueIterationSolver` (價值迭代演算法) 以及 `Visualizer` (使用 matplotlib 輸出圖檔)。
- `gridworld_result.png`: 由 `main.py` 腳本自動生成的政策 (Policy) 與價值 (Value) 矩陣結果圖。
- `requirements.txt`: Python 腳本所需的套件依賴 (numpy, matplotlib, seaborn)。
- `index.html`: 純前端互動式的 Demo 網頁。使用 Vanilla JS 重新實作了 Value Iteration 演算法，並提供可單步執行、自動收斂的動畫視覺化 UI。
- `log.md`: 完整的 AI 開發歷程與步驟紀錄。

## 環境設定 (Python)

### 參數：
- 網格大小：7x7
- 終點狀態：(0,0), (0,6), (6,0), (6,6), (3,3)
- 行動空間：上 (U)、下 (D)、左 (L)、右 (R)
- 轉移機率：確定性環境 (撞牆留在原地)
- Step Reward： -1.0
- Gamma (Discount Factor)：0.9

### 執行方式：

先安裝所需套件：
```bash
pip install -r requirements.txt
```

執行 Python 腳本進行價值迭代並輸出圖檔 `gridworld_result.png`：
```bash
python main.py
```

## 網頁互動版 Demo

請直接開啟 `index.html` 或前往 GitHub Pages 查看。
網頁提供了以下控制功能：
- **Step (單步執行)**：執行一次 Value Iteration 掃描 (Sweep)。
- **Run to Convergence**：自動連續執行直到最大變化量小於 1e-4，產生動畫效果。
- **Reset**：重置所有 Value 為 0，並清空 Policy 箭頭。
