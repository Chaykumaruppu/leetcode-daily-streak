# Day 031 – Minimum Absolute Difference (LeetCode 1200)

## 🧩 Problem Overview
You are given an array of distinct integers.  
The task is to find all pairs of elements with the minimum absolute difference between any two elements in the array.

Return the pairs in ascending order.

---

## 💡 Key Idea
The minimum absolute difference between elements will always occur between **adjacent elements in the sorted array**.

Sorting allows us to efficiently check only neighboring values instead of all pairs.

---

## 🛠️ Approach
1. Sort the array
2. Traverse adjacent elements and compute differences
3. Track the minimum difference found
4. Collect all pairs whose difference equals this minimum

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` (excluding output)

---

## 🧠 Concepts & Patterns Used
- Sorting
- Greedy scanning
- Adjacent comparison

---

## ✅ Status
- **Accepted**
- All test cases passed
- Optimal and clean solution

---

## 📌 Notes
This problem highlights how sorting simplifies pairwise comparison problems dramatically.
