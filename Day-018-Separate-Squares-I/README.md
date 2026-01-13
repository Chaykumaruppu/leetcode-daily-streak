# Day 18 – Separate Squares I-3453

## 🧩 Problem Overview
You are given multiple axis-aligned squares on a 2D plane.  
Each square is defined by the coordinates of its bottom-left corner and its side length.

The task is to find the **minimum y-coordinate of a horizontal line** such that:
- The **total area of squares above the line** equals
- The **total area of squares below the line**

Overlapping areas are counted multiple times.  
Answers within `1e-5` of the correct value are accepted.

---

## 💡 Key Idea
The total area difference between regions **above** and **below** the horizontal line is a **monotonic function** of `y`.

As the line moves upward:
- Area above **decreases**
- Area below **increases**

This monotonic behavior allows us to apply **Binary Search on the Answer**.

---

## 🛠️ Approach
1. Define a helper function `area_diff(y)` that computes:
2. For each square:
- Fully above the line → entire area contributes to `above`
- Fully below the line → entire area contributes to `below`
- Intersected by the line → split area proportionally
3. Perform binary search on `y` between:
- Minimum square bottom
- Maximum square top
4. Narrow the range until sufficient precision is achieved.

---

## ⏱️ Complexity Analysis
- **Time Complexity**: `O(n · log(precision))`
- **Space Complexity**: `O(1)`

Where `n` is the number of squares.

---

## 🧠 Concepts & Patterns Used
- Binary Search on Answer
- Geometry / Area computation
- Floating-point precision handling
- Monotonic functions

---

## ✅ Status
- **Accepted**
- All test cases passed
- Precision guaranteed within required tolerance

---

## 📌 Notes
This problem is a classic example of **binary search beyond integers**, commonly used in geometry and optimization interview problems.
