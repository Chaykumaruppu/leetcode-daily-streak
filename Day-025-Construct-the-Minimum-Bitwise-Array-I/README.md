# Day 025 – Construct the Minimum Bitwise Array I (LeetCode-3314)

## 🧩 Problem Overview
You are given an array of prime integers `nums`.  
For each index `i`, you must construct a value `ans[i]` such that the bitwise OR of `ans[i]` and `ans[i] + 1` equals `nums[i]`.  
Among all valid choices, `ans[i]` should be minimized. If no such value exists, return `-1` for that position.

---

## 💡 Key Idea
The expression `x | (x + 1)` sets all bits up to the least significant zero bit of `x`.  
To minimize `x` while achieving a target value, we attempt to remove the lowest set bit of `nums[i]`.  
If `nums[i]` is of the form `2^k`, no such `x` exists because the OR operation cannot reproduce a single-bit number.

---

## 🛠️ Approach
1. For each number `n` in `nums`:
   - If `n` is a power of two, return `-1`
   - Otherwise, compute `n & (n - 1)` to clear the lowest set bit
2. This value produces the minimum valid `ans[i]`
3. Collect results into the output array

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` (excluding output array)

Each element is processed independently using constant-time bit operations.

---

## 🧠 Concepts & Patterns Used
- Bit Manipulation
- Bitwise OR properties
- Power-of-two detection
- Greedy minimization

---

## ✅ Status
- **Accepted**
- All test cases passed
- Meets problem constraints efficiently

---

## 📌 Notes
This problem reinforces how subtle bitwise properties can drastically simplify what initially appears to be a search problem.
