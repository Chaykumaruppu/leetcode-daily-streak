# Day 2 – Count Negative Numbers in a Sorted Matrix-1351

## Problem Summary
Given a matrix sorted in non-increasing order both row-wise and column-wise,
count the total number of negative numbers.

## Approach
- Start from the top-right corner of the matrix.
- If the current value is negative, all values below it in the same column
  are also negative.
- Count them and move left.
- If the value is non-negative, move down.

## Key Concepts
- Matrix traversal
- Two-pointer technique
- Monotonic properties

## Time & Space Complexity
- Time: O(m + n)
- Space: O(1)
