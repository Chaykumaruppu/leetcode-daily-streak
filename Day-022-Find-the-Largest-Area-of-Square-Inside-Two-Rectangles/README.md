# Day 022 – Find the Largest Area of Square Inside Two Rectangles (LeetCode-3047)

## 🧩 Problem Overview
You are given multiple axis-aligned rectangles in a 2D plane, each defined by bottom-left and top-right coordinates.  
The task is to determine the **maximum possible area of a square** that can fit completely inside the **intersection region of at least two rectangles**.  
If no two rectangles intersect, the result should be `0`.

---

## 💡 Key Idea
A valid square can only exist inside the **overlapping region** of rectangles.  
For any pair of rectangles, if their intersection forms a valid rectangle, the largest square that fits inside it will have a side length equal to the **minimum of the intersection’s width and height**.

---

## 🛠️ Approach
1. Iterate over all pairs of rectangles.
2. Compute the intersection rectangle for each pair.
3. If the intersection is valid:
   - Calculate width and height.
   - The maximum square side is `min(width, height)`.
4. Track and update the maximum square area.
5. Return the maximum area found.

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O(n²)` — all rectangle pairs are checked  
- **Space Complexity**: `O(1)` — constant extra space

This approach is efficient for `n ≤ 1000`.

---

## 🧠 Concepts & Patterns Used
- Geometry
- Rectangle intersection
- Brute-force optimization
- Coordinate comparison

---

## ✅ Status
- **Accepted**
- All test cases passed
- Meets problem constraints

---

## 📌 Notes
This problem sharpens geometric intuition and intersection handling — a common pattern in interview-level spatial problems.
