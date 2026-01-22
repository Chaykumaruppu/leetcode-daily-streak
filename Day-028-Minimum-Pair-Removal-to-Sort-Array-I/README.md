# Day 028 – Minimum Pair Removal to Sort Array I (LeetCode-3507)

## 🧩 Problem Overview
You are given an integer array `nums`. You can repeatedly:
- Select the adjacent pair with the minimum sum
- Replace that pair with their sum

The goal is to determine the **minimum number of operations** required to make the array **non-decreasing**.

---

## 💡 Key Idea
Each operation reduces the array size while increasing local values.  
The array becomes non-decreasing once all adjacent inversions are eliminated.

The process essentially simulates **greedy merging** of the smallest adjacent pairs until the order constraint is satisfied.

---

## 🛠️ Approach
1. While the array is not non-decreasing:
   - Find the adjacent pair with the minimum sum
   - Replace the pair with their sum
   - Increment operation count
2. Repeat until the array becomes sorted (non-decreasing)
3. Return the total number of operations performed

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O(n²)`
- **Space Complexity**: `O(n)`

Given the small constraints (`n ≤ 50`), this approach is efficient enough.

---

## 🧠 Concepts & Patterns Used
- Greedy
- Array Simulation
- Adjacent Pair Processing

---

## ✅ Status
- **Accepted**
- All test cases passed
- Fully compliant with problem constraints

---

## 📌 Notes
This problem highlights how controlled greedy merges can enforce global ordering through local decisions.
