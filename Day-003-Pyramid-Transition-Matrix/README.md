# Day 3 – Pyramid Transition Matrix-756

## Problem Summary
Given a bottom row and allowed triangular transitions, determine whether
a pyramid can be built up to the top following the rules.

## Approach
- Use DFS with backtracking.
- Map each allowed pair to possible top blocks.
- Use memoization to prune repeated failing states.

## Key Concepts
- Depth First Search
- Backtracking
- Memoization

## Time & Space Complexity
- Time: Exponential (pruned heavily)
- Space: O(states)
