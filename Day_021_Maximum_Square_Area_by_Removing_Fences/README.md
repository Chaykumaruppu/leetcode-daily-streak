# Day 021 – Maximum Square Area by Removing Fences From a Field (LeetCode-2975)

## 🧩 Problem Overview
You are given a rectangular field with removable horizontal and vertical fences.
Each fence lies on a specific coordinate, and removing fences creates larger rectangular regions.
The task is to determine the **maximum possible area of a square** that can be formed after removing some fences, or return `-1` if no square is possible.

---

## 💡 Key Idea
A square can only be formed if **both height and width gaps are equal**.
So instead of simulating removals, we:
- Compute all possible **consecutive gaps** between fences
- Look for the **largest common gap** between horizontal and vertical directions

This transforms the problem into a **gap comparison problem**.

---

## 🛠️ Approach
1. Add boundary fences (`1` and `m / n`) to both horizontal and vertical fence lists.
2. Sort the fence positions.
3. Compute all possible distances between fence pairs.
4. Store horizontal gaps in a set for fast lookup.
5. Traverse vertical gaps and find the largest gap that also exists horizontally.
6. Square the largest valid side length to get the area.

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O(H² + V²)`
- **Space Complexity**: `O(H²)`  
Where `H` and `V` are the number of horizontal and vertical fences.

---

## 🧠 Concepts & Patterns Used
- Geometry
- Set-based lookup
- Difference arrays
- Brute-force optimization via hashing

---

## ✅ Status
- **Accepted**
- All test cases passed
- Works within constraints and modulo conditions

---

## 📌 Notes
Key insight: **area maximization reduces to finding the largest common gap** — not simulation.
