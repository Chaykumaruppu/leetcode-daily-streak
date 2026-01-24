# Day 029 – Minimize Maximum Pair Sum in Array (LeetCode 1877)

## 🧩 Problem Overview
You are given an array of integers of even length. The task is to divide the array into pairs such that:
- Each element belongs to exactly one pair
- The maximum pair sum among all pairs is minimized

Return the minimized maximum pair sum after optimal pairing.

---

## 💡 Key Idea
To minimize the maximum pair sum:
- Pair the smallest element with the largest
- Pair the second smallest with the second largest, and so on

This greedy pairing balances large values with small ones, preventing any pair from becoming excessively large.

---

## 🛠️ Approach
1. Sort the array in ascending order
2. Use two pointers:
   - One at the beginning
   - One at the end
3. Pair elements from both ends and track the maximum sum encountered
4. Continue until all elements are paired

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O(n log n)` due to sorting
- **Space Complexity**: `O(1)` excluding sorting overhead

---

## 🧠 Concepts & Patterns Used
- Greedy strategy
- Two-pointer technique
- Sorting

---

## ✅ Status
- **Accepted**
- All test cases passed
- Optimal solution

---

## 📌 Notes
This problem is a classic greedy pairing problem and commonly appears in interviews to test sorting and pairing intuition.
