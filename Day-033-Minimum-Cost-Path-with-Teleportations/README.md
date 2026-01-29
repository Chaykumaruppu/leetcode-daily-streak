# Day 033 – Minimum Cost Path with Teleportations (LeetCode 3651)

## 🧩 Problem Overview
You are given a 2D grid where each cell contains a cost.
You start at the top-left cell `(0,0)` and must reach the bottom-right cell `(m-1, n-1)`.

You can:
- Move **right** or **down** normally (paying the destination cell cost)
- Use **teleportation** up to `k` times:
  - Teleport from `(i, j)` to `(x, y)` if `grid[i][j] == grid[x][y]`
  - Teleportation cost is `0`

The task is to compute the **minimum total cost** to reach the destination.

---

## 💡 Key Idea
This is a **dynamic programming + optimization** problem.

Key observations:
- Normal movement is monotonic (right & down)
- Teleportation allows zero-cost jumps between equal-valued cells
- Teleportations are limited (`k` times), so DP must track usage count

---

## 🛠️ Approach
1. Use a 3D DP array:
   - `dp[t][i][j]` = minimum cost to reach cell `(i, j)` using `t` teleportations
2. First compute base DP for normal movements
3. Group grid cells by value to efficiently handle teleportation
4. For each teleportation count:
   - Relax costs across same-valued cells
   - Re-run row/column transitions to propagate improvements
5. The answer is the minimum cost at `(m-1, n-1)` over all teleport counts

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O(k * m * n)`
- **Space Complexity**: `O(k * m * n)`

Efficient enough under given constraints.

---

## 🧠 Concepts & Patterns Used
- Dynamic Programming (Multi-State)
- Grid DP
- State Compression
- Optimization via Value Grouping
- Teleportation Modeling

---

## ✅ Status
- **Accepted**
- All test cases passed
- Correct handling of teleport limits

---

## 📌 Notes
This problem is a strong example of how adding a constraint (`k` teleports)
turns a simple grid DP into a multi-dimensional optimization problem.
