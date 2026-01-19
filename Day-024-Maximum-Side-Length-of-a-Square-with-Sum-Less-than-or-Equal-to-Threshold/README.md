# Day 024 – Maximum Side Length of a Square with Sum ≤ Threshold (LeetCode-1292)

## 🧩 Problem Overview
You are given a 2D matrix of non-negative integers and an integer `threshold`.
The task is to determine the **maximum possible side length** of a square submatrix
whose total sum is **less than or equal to the threshold**.
If no such square exists, return `0`.

---

## 💡 Key Idea
Brute-force checking all square submatrices is inefficient.
By using **2D prefix sums**, we can compute the sum of any square in constant time.
This allows us to apply **binary search on the side length** to efficiently find
the maximum valid square.

---

## 🛠️ Approach
1. Construct a 2D prefix sum matrix for fast area sum queries.
2. Binary search on the possible side length `k`.
3. For each candidate `k`, check all `k × k` submatrices using prefix sums.
4. If any square satisfies the threshold, try larger sizes.
5. Otherwise, reduce the search space.

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O(m × n × log(min(m, n)))`
- **Space Complexity**: `O(m × n)`

Prefix sums allow constant-time submatrix sum calculation.

---

## 🧠 Concepts & Patterns Used
- 2D Prefix Sum
- Binary Search on Answer
- Sliding Window over Matrix
- Optimization over Brute Force

---

## ✅ Status
- **Accepted**
- All test cases passed
- Efficient and within constraints

---

## 📌 Notes
This problem is a classic example of combining prefix sums with binary search,
a highly reusable pattern in matrix-based interview problems.
