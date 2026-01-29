# Day 032 – Minimum Cost Path with Edge Reversals (LeetCode 3650)

## 🧩 Problem Overview
You are given a directed, weighted graph with `n` nodes and a list of edges.
Each node has a one-time switch that allows reversing **one incoming edge**
and immediately traversing it at **double the original cost**.
The goal is to find the minimum cost to travel from node `0` to node `n-1`.

---

## 💡 Key Idea
The key insight is that the edge-reversal rule can be modeled directly
inside the graph itself.

- A normal edge `u → v` with cost `w` remains unchanged
- A reversed edge is equivalent to `v → u` with cost `2 * w`

With this transformation, the problem reduces to finding the shortest path
in a graph with modified edge weights using **Dijkstra’s algorithm**.

---

## 🛠️ Approach
1. Build an adjacency list:
   - Add original directed edges with cost `w`
   - Add reversed edges with cost `2w`
2. Run Dijkstra’s algorithm starting from node `0`
3. Use a min-heap to always expand the lowest-cost path
4. Stop when node `n-1` is reached
5. Return the minimum cost or `-1` if unreachable

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O((V + E) log V)`
- **Space Complexity**: `O(V + E)`

This is optimal for weighted shortest-path problems.

---

## 🧠 Concepts & Patterns Used
- Graph Modeling
- Dijkstra’s Algorithm
- Priority Queue (Min Heap)
- Greedy Shortest Path
- Graph Transformation

---

## ✅ Status
- **Accepted**
- All test cases passed (`699 / 699`)
- Efficient within time and memory limits

---

## 📌 Notes
A seemingly complex state-based graph problem becomes much simpler
once edge reversals are treated as weighted reverse edges.
This is a great example of **problem transformation**.
