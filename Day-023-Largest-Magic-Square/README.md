# Day 023 – Largest Magic Square (LeetCode)

## 🧩 Problem Overview
You are given an `m x n` grid of integers.  
A **k × k magic square** is a square subgrid where:
- All row sums are equal
- All column sums are equal
- Both diagonal sums are equal  

The task is to find and return the **largest possible side length `k`** of such a magic square present in the grid.

---

## 💡 Key Idea
Directly checking every possible square by recomputing sums is inefficient.  
The core idea is to **precompute prefix sums** for rows, columns, and both diagonals so that:
- Any row, column, or diagonal sum can be queried in constant time
- Each candidate square can be validated efficiently

---

## 🛠️ Approach
1. Build prefix sum matrices for:
   - Rows
   - Columns
   - Main diagonal
   - Anti-diagonal
2. Iterate over possible square sizes from largest to smallest.
3. For each possible top-left position:
   - Check all row sums
   - Check all column sums
   - Check both diagonal sums
4. Return the first valid (largest) magic square size found.
5. If no larger square exists, return `1` (every single cell is trivially a magic square).

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O(min(m, n)³)`
- **Space Complexity**: `O(m × n)`

Prefix sums allow constant-time validation of sums, keeping the solution efficient.

---

## 🧠 Concepts & Patterns Used
- 2D Prefix Sums
- Matrix Traversal
- Diagonal Sum Computation
- Optimization over Brute Force
- Geometry in Grids

---

## ✅ Status
- **Accepted**
- All test cases passed
- Meets problem constraints efficiently

---

## 📌 Notes
This problem is a strong example of how prefix sums transform an otherwise brute-force grid problem into an efficient and interview-friendly solution.

