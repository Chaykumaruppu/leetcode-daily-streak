# Day 030 – Minimum Difference Between Highest and Lowest of K Scores (LeetCode 1984)

## 🧩 Problem Overview
You are given an integer array where each element represents a student's score.  
Given an integer `k`, select any `k` students such that the difference between the highest and lowest scores among them is minimized.

Return the minimum possible difference.

---

## 💡 Key Idea
After sorting the scores, any optimal group of `k` students must form a **contiguous window** in the sorted array.  
This allows us to efficiently compare all possible groups of size `k`.

---

## 🛠️ Approach
1. If `k == 1`, the difference is always `0`
2. Sort the array of scores
3. Slide a window of size `k` across the sorted array
4. Track the minimum difference between the first and last elements of each window

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O(n log n)` due to sorting
- **Space Complexity**: `O(1)` excluding sort overhead

---

## 🧠 Concepts & Patterns Used
- Sorting
- Sliding Window
- Greedy optimization

---

## ✅ Status
- **Accepted**
- All test cases passed
- Optimal solution

---

## 📌 Notes
This is a classic sliding window problem that highlights how sorting simplifies range-based optimizations.
