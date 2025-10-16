# <u>**Keyboard Optimization**

The goal of this assignment is to use optimization technique such as Simulated Annealing in order to optimize keyboard layouts with the goal of reducing typing distance when typing a given text.

**Steps for optimization problem:**

-Start with the qwerty layout that was given as an example in the A4 assignment.
-Keep the same locations ((x, y) coordinates) for the keys, but allow each key to be swapped or moved into a different location. With this as the basic "move", write an optimization routine to test the quality of different keyboard layouts.

**Features of the function:** 
- should be able to take in any arbitrary string (can be a multi-line string) as text, and go through and optimize the layout for that string.
- provide visualizations for the final keyboard layout, and also to show how the total distance cost decreases as you optimize.
- The main problem statement only requires you to optimize for the qwerty locations.
