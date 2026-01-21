# Day 026 – Construct the Minimum Bitwise Array II (LeetCode-3315)

## 🧩 Problem Overview
You are given an array `nums`. For each index `i`, you must construct a value `ans[i]` such that:
- `ans[i] OR (ans[i] + 1) == nums[i]`
- `ans[i]` is minimized
- If no such value exists, return `-1` for that index

The task is to compute the resulting array efficiently for all elements.

---

## 💡 Key Idea
The bitwise OR of two consecutive numbers depends on the trailing `1`s in the binary representation.
- If a number is **even**, no valid value exists.
- If a number is **odd**, the smallest valid value can be derived by removing the highest contributing trailing bit.

This allows a direct mathematical construction instead of brute force.

---

## 🛠️ Approach
1. Iterate through each value in `nums`
2. If the value is even, append `-1`
3. Otherwise:
   - Count the number of trailing `1`s in binary form
   - Subtract `2^(k-1)` from the number to get the minimum valid result
4. Collect results into the output array

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O(n * log(max(nums)))`
- **Space Complexity**: `O(1)` (excluding output array)

---

## 🧠 Concepts & Patterns Used
- Bit Manipulation
- Binary Representation
- Greedy Construction

---

## ✅ Status
- **Accepted**
- All test cases passed
- Meets problem constraints exactly

---

## 📌 Notes
This problem reinforces how bitwise patterns can eliminate brute-force approaches entirely when understood correctly.
