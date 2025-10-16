# <u> **Keyboard Analysis - Assignment 4**
The goal of this assignment is to develop a python program that analyzes keyboard usage patterns for a given text input. The program
should generate a heatmap visualization of key usage and calculate the total distance traveled by
fingers while typing.

An example of this can be seen at https://www.patrick-wied.at/projects/heatmap-keyboard/
- As a key is used more and more often, the colour allocated for it tends towards the high end of the heatmap (red).
- Less used keys are towards the violet end. The colors are blended to create a smooth heatmap.
  The keyboard layout is represented as a **2D coordinate system**, where:

- Each key has a position `(x, y)`.
- The **home row keys** serve as starting positions for all fingers.
- The x-coordinate increases from left to right, and the y-coordinate increases from bottom to top.

For each character typed:

1. Identify the starting position (home key) and target key.
2. Calculate the **Euclidean distance** between these points.
3. For characters requiring the Shift key, include the distance to/from Shift.

**Example (QWERTY):**

- Typing `'y'`:
  - Start: `j` at `(7.75, 2)`
  - End: `y` at `(6.5, 3)`
  - Distance: `≈1.60 units`
- Typing `'T'` (Shift + t):
  - Distance to Shift: `2.01 units`
  - Distance to `t`: `1.25 units`
  - Total distance: `3.26 units`

> Note: Only **one-way distances** are considered (finger return is ignored).

---

## Features

1. **Input**
   - Keyboard layout specification (e.g., QWERTY, Dvorak, Colemak)
   - Text string to analyze

2. **Key Usage Analysis**
   - Counts frequency of each key press
   - Generates a **heatmap visualization** of key usage
   - Accounts for **Shift key** for uppercase letters and special characters

3. **Finger Travel Distance**
   - Calculates distance traveled for each character
   - Sums the total finger travel distance
   - Includes travel to/from Shift key for uppercase letters

4. **Output**
   - Heatmap image of key usage
   - Total finger travel distance for the input text

5. **Optional / Bonus**
   - Animated typing visualization
   - Suggest optimized keyboard layouts based on input text (see keyboard optimizations)

---


