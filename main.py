import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns
from typing import Tuple, List, Dict

class GridWorld:
    """
    7x7 Gridworld Environment.
    Terminal states: (0,0), (0,6), (6,0), (6,6), (3,3).
    Deterministic transitions, bump into wall stays in place.
    Step reward: -1.
    """
    def __init__(self, size: int = 7, step_reward: float = -1.0):
        self.size = size
        self.step_reward = step_reward
        self.terminals = [(0, 0), (0, 6), (6, 0), (6, 6), (3, 3)]
        
        # Actions: Up, Down, Left, Right
        # represented as (d_row, d_col)
        self.actions = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }
        
    def is_terminal(self, state: Tuple[int, int]) -> bool:
        """Check if a state is a terminal state."""
        return state in self.terminals

    def step(self, state: Tuple[int, int], action: str) -> Tuple[Tuple[int, int], float]:
        """
        Takes a step in the environment.
        Returns: (next_state, reward)
        """
        if self.is_terminal(state):
            return state, 0.0

        r, c = state
        dr, dc = self.actions[action]
        next_r = r + dr
        next_c = c + dc

        # Check boundaries (bump into wall -> stay in place)
        if next_r < 0 or next_r >= self.size or next_c < 0 or next_c >= self.size:
            next_state = state
        else:
            next_state = (next_r, next_c)

        return next_state, self.step_reward

class ValueIterationSolver:
    """Value Iteration algorithm solver for GridWorld."""
    def __init__(self, env: GridWorld, gamma: float = 0.9, theta: float = 1e-4):
        self.env = env
        self.gamma = gamma
        self.theta = theta
        self.V = np.zeros((env.size, env.size))
        self.policy = np.full((env.size, env.size), '', dtype=object)

    def solve(self):
        """Runs the value iteration algorithm until convergence."""
        iteration = 0
        while True:
            delta = 0.0
            new_V = np.copy(self.V)
            for r in range(self.env.size):
                for c in range(self.env.size):
                    state = (r, c)
                    if self.env.is_terminal(state):
                        new_V[r, c] = 0.0
                        continue
                    
                    action_values = []
                    for action in self.env.actions:
                        next_state, reward = self.env.step(state, action)
                        val = reward + self.gamma * self.V[next_state[0], next_state[1]]
                        action_values.append(val)
                    
                    best_value = max(action_values)
                    delta = max(delta, abs(best_value - self.V[r, c]))
                    new_V[r, c] = best_value
                    
            self.V = new_V
            iteration += 1
            if iteration % 10 == 0:
                print(f"Iteration {iteration}, delta={delta}")
            if delta < self.theta:
                print(f"Converged at iteration {iteration}")
                break
                
        self._extract_policy()
        return self.V, self.policy

    def _extract_policy(self):
        """Extracts the greedy policy after value iteration converges."""
        for r in range(self.env.size):
            for c in range(self.env.size):
                state = (r, c)
                if self.env.is_terminal(state):
                    self.policy[r, c] = 'T'
                    continue
                
                best_val = -float('inf')
                best_actions = []
                
                for action in self.env.actions:
                    next_state, reward = self.env.step(state, action)
                    val = reward + self.gamma * self.V[next_state[0], next_state[1]]
                    
                    # Small tolerance for floating point comparison
                    if val > best_val + 1e-8:
                        best_val = val
                        best_actions = [action]
                    elif abs(val - best_val) < 1e-8:
                        best_actions.append(action)
                
                self.policy[r, c] = ''.join(best_actions)

class Visualizer:
    """Visualizes the Value Matrix and Policy Matrix."""
    def __init__(self, env: GridWorld, V: np.ndarray, policy: np.ndarray):
        self.env = env
        self.V = V
        self.policy = policy
        
    def _draw_policy_arrows(self, ax, r, c, cell_policy):
        """Helper to draw arrows based on policy string."""
        if 'T' in cell_policy:
            return
            
        # Draw small arrows or lines for each action
        x, y = c, r
        arrow_len = 0.3
        
        # Flip y axis conceptually since row 0 is at top, but matplotlib coordinates
        # depend on how we plot it. We'll use quiver or simple annotate
        for a in cell_policy:
            if a == 'U':
                dx, dy = 0, -arrow_len
            elif a == 'D':
                dx, dy = 0, arrow_len
            elif a == 'L':
                dx, dy = -arrow_len, 0
            elif a == 'R':
                dx, dy = arrow_len, 0
                
            ax.annotate('', xy=(x + 0.5 + dx, y + 0.5 + dy), 
                        xytext=(x + 0.5, y + 0.5), 
                        arrowprops=dict(arrowstyle="->", color="black", lw=1.2))

    def save_plot(self, filename: str = "gridworld_result.png"):
        """Saves the visualization to a file."""
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # --- Left: Value Matrix ---
        ax1 = axes[0]
        # Create a mask to color terminal states dark grey
        mask = np.zeros_like(self.V, dtype=bool)
        for tr, tc in self.env.terminals:
            mask[tr, tc] = True
            
        sns.heatmap(self.V, annot=True, fmt=".2f", cmap="Blues", cbar=False, ax=ax1, 
                    linewidths=1, linecolor='steelblue', mask=mask,
                    annot_kws={"color": "black", "size": 10})
        
        # Color terminal states dark grey
        for tr, tc in self.env.terminals:
            ax1.add_patch(plt.Rectangle((tc, tr), 1, 1, fill=True, color='dimgrey'))

        ax1.set_title("Value Matrix")
        # Ensure axis displays ticks correctly
        ax1.set_xticks(np.arange(self.env.size) + 0.5)
        ax1.set_yticks(np.arange(self.env.size) + 0.5)
        ax1.set_xticklabels(np.arange(self.env.size))
        ax1.set_yticklabels(np.arange(self.env.size))

        # --- Right: Policy Matrix ---
        ax2 = axes[1]
        
        # Create empty heatmap for grid lines
        sns.heatmap(np.zeros_like(self.V), annot=False, cmap=ListedColormap(['white']), cbar=False, ax=ax2,
                    linewidths=1, linecolor='steelblue', mask=mask)
                    
        # Color terminal states
        for tr, tc in self.env.terminals:
            ax2.add_patch(plt.Rectangle((tc, tr), 1, 1, fill=True, color='dimgrey'))
            
        for r in range(self.env.size):
            for c in range(self.env.size):
                if not mask[r, c]:
                    self._draw_policy_arrows(ax2, r, c, self.policy[r, c])
                    
        ax2.set_title("Policy Matrix")
        ax2.set_xticks(np.arange(self.env.size) + 0.5)
        ax2.set_yticks(np.arange(self.env.size) + 0.5)
        ax2.set_xticklabels(np.arange(self.env.size))
        ax2.set_yticklabels(np.arange(self.env.size))

        plt.tight_layout()
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()

if __name__ == "__main__":
    env = GridWorld()
    solver = ValueIterationSolver(env)
    V, policy = solver.solve()
    
    vis = Visualizer(env, V, policy)
    vis.save_plot()
    print("Value iteration complete. Result saved to gridworld_result.png")
