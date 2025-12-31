# Day 5 – Last Day Where You Can Still Cross-1970

## Problem Summary
Find the last day when it is possible to cross from the top to the bottom
of a grid using only land cells.

## Approach
- Binary search on the day.
- For each day, simulate flooding and check reachability using BFS.

## Key Concepts
- Binary search on answer
- Breadth-first search
- Grid traversal

## Time & Space Complexity
- Time: O(R * C * log(R * C))
- Space: O(R * C)
