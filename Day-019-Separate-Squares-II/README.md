# 📘 Day 19 – Separate Squares II (LeetCode 3454)

## 🔍 Problem Overview
You are given a set of axis-aligned squares on a 2D plane. Each square is defined by its bottom-left coordinate and side length.

Your task is to find the **minimum y-coordinate of a horizontal line** such that:

- The **total area covered by squares above the line**
- is **equal to**
- the **total area covered by squares below the line**

### Important Notes
- Squares **may overlap**
- **Overlapping areas are counted only once**
- Answers within **1e-5 precision** are accepted

---

## 🧠 Key Insight
This problem reduces to splitting the **union area** of multiple squares into two equal halves using a horizontal cut.

To achieve this efficiently:
- Apply a **Sweep Line Algorithm** along the Y-axis
- Maintain active X-intervals using a **Segment Tree**
- Use **coordinate compression** to handle large ranges
- Accumulate area slice-by-slice until half of the total area is reached

---

## ⚙️ Approach

### 1️⃣ Sweep Line on Y-axis
- For each square, generate two events:
  - Entry event at `y`
  - Exit event at `y + side`
- Sort all events by their Y-coordinate

### 2️⃣ Segment Tree on X-axis
- Tracks active x-intervals
- Maintains the **union width** of overlapping intervals
- Supports efficient add/remove operations

### 3️⃣ Area Accumulation
- First compute the **total union area**
- Sweep again and accumulate area between consecutive Y-events
- When accumulated area reaches half, interpolate the exact Y value

---

## ⏱ Complexity Analysis

| Metric | Value |
|------|------|
| Time Complexity | **O(N log N)** |
| Space Complexity | **O(N)** |
| Precision | **≤ 1e-5** |

---

## 🧩 Concepts Used
- Sweep Line Algorithm  
- Segment Tree  
- Coordinate Compression  
- Computational Geometry  
- Area Accumulation  

---

## 🏁 Final Status
✔ Accepted  
✔ All test cases passed  
✔ Time Limit Safe  

---

## 🚀 Daily Streak
**Day 19 completed** — solved a hard geometry problem using an optimal sweep-line solution.
