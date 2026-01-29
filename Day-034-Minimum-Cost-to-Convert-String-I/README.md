# Day 034 – Minimum Cost to Convert String I (LeetCode 2976)

## 🧩 Problem Overview
You are given two strings `source` and `target` of equal length.
You can convert characters using a set of allowed transformations, each with an associated cost.

Each conversion may be applied multiple times, and indirect conversions are allowed.
The goal is to find the **minimum total cost** to convert `source` into `target`.

Return `-1` if conversion is impossible.

---

## 💡 Key Idea
This problem reduces to finding **minimum conversion cost between characters**.

Key insight:
- There are only **26 lowercase letters**
- Conversion rules form a **directed weighted graph**
- We must compute **all-pairs shortest paths** between characters

---

## 🛠️ Approach
1. Build a `26 x 26` cost matrix
2. Initialize:
   - `dist[i][i] = 0`
   - Given conversions with minimum cost
3. Apply **Floyd–Warshall** to compute shortest conversion paths
4. For each position:
   - Add cost to convert `source[i] → target[i]`
   - If unreachable → return `-1`

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O(26³ + n)`
- **Space Complexity**: `O(26²)`

Highly efficient and constant-bounded.

---

## 🧠 Concepts & Patterns Used
- Graph Modeling
- Floyd–Warshall Algorithm
- All-Pairs Shortest Path
- Cost Optimization

---

## ✅ Status
- **Accepted**
- All test cases passed
- Handles indirect conversions correctly

---

## 📌 Notes
Classic example of transforming a string using graph shortest-path preprocessing.
