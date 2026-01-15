# Day 20 – Maximize Area of Square Hole in Grid (LeetCode 2943)

## 🧩 Problem Overview
You are given a grid formed by horizontal and vertical bars. Some of these bars can be removed to create empty regions (holes).  
The goal is to determine the **maximum possible area of a square-shaped hole** that can be formed after removing any number of removable bars.

---

## 💡 Key Insight
- Removing **k consecutive bars** creates a continuous gap of **k + 1 units**
- A square hole requires **equal horizontal and vertical spans**
- Therefore, the largest square hole is limited by the **minimum of the maximum horizontal and vertical gaps**

---

## 🛠️ Approach
1. Sort the removable horizontal bars and find the **longest consecutive sequence**
2. Repeat the same for vertical bars
3. Convert gaps to usable lengths by adding `+1`
4. The square side length is the minimum of the two
5. Return `side × side`

---

## 🧠 Algorithm
- Scan bar indices to detect consecutive sequences
- Track the maximum length of such sequences
- Compute the square area based on the smallest dimension

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(H log H + V log V)`
- **Space Complexity:** `O(1)` (excluding input storage)

---

## ✅ Final Notes
- Handles edge cases where no bars are removed
- Fully compliant with LeetCode’s Python runtime
- Efficient and scalable for large inputs

---

📅 **Streak Status:** Day 20 completed successfully  
🔥 **Consistency maintained**
