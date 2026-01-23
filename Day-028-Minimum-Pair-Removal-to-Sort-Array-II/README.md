# Day 028 – Minimum Pair Removal to Sort Array II (LeetCode 3510)

## 🧩 Problem Overview
You are given an integer array `nums`. In one operation, you may select the adjacent pair with the minimum sum (choosing the leftmost one if there are multiple) and replace the pair with their sum.

The goal is to determine the **minimum number of such operations** required to make the array **non-decreasing**.

An array is non-decreasing if every element is greater than or equal to the previous one.

---

## 💡 Key Idea
Each operation merges two adjacent elements, effectively shrinking the array.  
The challenge lies in **always selecting the valid minimum-sum pair** while **accurately tracking inversions** that violate the non-decreasing order.

A naive greedy or LIS-based approach fails due to dynamic changes in adjacency after merges.

The correct solution requires:
- Precise simulation of the process
- Efficient tracking of adjacent pairs
- Careful inversion updates after each merge

---

## 🛠️ Approach
1. Treat the array as a **doubly linked list** using index-based `left` and `right` pointers.
2. Maintain a **min-heap** of adjacent pair sums.
3. Track the number of **inversions** (positions where `nums[i] > nums[i+1]`).
4. While inversions exist:
   - Extract the smallest valid adjacent pair from the heap.
   - Merge the pair and update neighbors.
   - Adjust inversion count only for affected indices.
5. Continue until the array becomes non-decreasing.

This ensures correctness while maintaining efficiency.

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O(n log n)`
  - Each merge involves heap operations and constant-time pointer updates.
- **Space Complexity**: `O(n)`
  - For heap storage and auxiliary arrays.

---

## 🧠 Concepts & Patterns Used
- Greedy simulation
- Min-heap (priority queue)
- Doubly linked list via arrays
- Inversion counting
- Careful state validation (to avoid stale heap entries)

---

## ✅ Status
- **Accepted**
- All test cases passed
- Handles negative values and edge cases correctly

---

## 📌 Notes
This is a genuinely hard problem where many intuitive solutions fail.  
Correctness depends on precise local updates rather than global heuristics.
