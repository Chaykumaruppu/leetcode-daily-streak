# Day 4 – Magic Squares in Grid-840

## Problem Summary
Count how many 3×3 subgrids form a magic square.

## Approach
- Slide a 3×3 window across the grid.
- Check center is 5.
- Ensure values are 1–9 and unique.
- Validate row, column, and diagonal sums.

## Key Concepts
- Grid traversal
- Pruning
- Condition checking

## Time & Space Complexity
- Time: O(m × n)
- Space: O(1)
