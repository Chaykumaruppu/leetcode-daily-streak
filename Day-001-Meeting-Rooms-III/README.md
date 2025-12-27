# Day 1 – Meeting Rooms III (LeetCode)

## Problem Summary
You are given n rooms and a list of meetings with start and end times.
Meetings must be assigned to the lowest indexed available room.
If no room is free, the meeting is delayed while keeping its duration unchanged.

## Approach
- Use two min-heaps:
  1. Available rooms (sorted by room index)
  2. Occupied rooms (sorted by meeting end time)
- Free rooms when meetings end.
- Assign the lowest indexed available room.
- If all rooms are busy, delay the meeting until the earliest room becomes free.

## Key Concepts
- Greedy Scheduling
- Priority Queue (Min Heap)
- Simulation

## Time & Space Complexity
- Time Complexity: O(M log N)
- Space Complexity: O(N)

## Notes
Implemented without Python type hints to ensure compatibility with older runtimes.
