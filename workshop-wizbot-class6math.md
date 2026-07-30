# CBSE Class 6 Math Block Coding Projects with Wizbot Maxx

Wizbot Maxx is a screen-free robot toy that combines hands-on play with block-based coding. It supports both button-based programming for younger kids and PictoBlox block coding for ages 8+. The following 10 projects are designed for CBSE Class 6 students, each focusing on specific coding concepts while integrating mathematical thinking.


## Project 1: Number Line Jumps

**Concepts:** Variables, Loops, Output

**Objective:** Program Wizbot to jump forward a specific number of steps stored in a variable.

**Description:** Create a variable called `steps` and set it to a value (e.g., 5). Use a loop to make Wizbot move forward that many times. Students learn that variables store values that can be used multiple times in a program.

**Math Connection:** Number line concepts, counting, addition.

**PictoBlox Blocks:**
- `when green flag clicked` (Events)
- `set [steps] to [5]` (Variables)
- `repeat [steps]` (Control/Loops)
  - `move forward [1] step` (Motion)


## Project 2: Multiplication Dance

**Concepts:** Variables, Loops, Counters, Output

**Objective:** Wizbot performs a dance move a number of times equal to a multiplication fact.

**Description:** Set two variables—`number1` and `number2`. Multiply them (using a variable for the product) and use a loop to make Wizbot move forward that many times. For example, if `number1 = 3` and `number2 = 4`, the product is 12, so Wizbot moves 12 steps.

**Math Connection:** Multiplication tables, repeated addition.

**PictoBlox Blocks:**
- `when green flag clicked`
- `set [number1] to [3]`
- `set [number2] to [4]`
- `set [product] to [number1 * number2]`
- `repeat [product]`
  - `move forward [1] step`


## Project 3: Even-Odd Path Finder

**Concepts:** Conditional Statements (If-Else), Modulus Operator (%), Comparison Operators, Boolean Logic, Input

**Objective:** Wizbot takes a different path based on whether a number is even or odd.

**Description:** The user inputs a number. Using the modulus operator (`number % 2`), the program checks if the remainder is 0. If true (even), Wizbot turns right and moves forward. If false (odd), Wizbot turns left and moves forward.

**Math Connection:** Even/odd numbers, divisibility, remainders.

**PictoBlox Blocks:**
- `when green flag clicked`
- `ask [Enter a number:] and wait` (Input)
- `set [num] to [answer]`
- `if [num % 2 = 0] then` (Conditional + Modulus + Comparison)
  - `turn right [90] degrees`
  - `move forward [5] steps`
- `else`
  - `turn left [90] degrees`
  - `move forward [5] steps`


## Project 4: Random Shape Drawer

**Concepts:** Random Number Generation, Loops, Variables, Output

**Objective:** Wizbot draws a shape with a random number of sides.

**Description:** Generate a random number between 3 and 8 (representing sides of a polygon). Use a loop to draw that shape by repeating forward movements and turns. The number of sides determines the turn angle (`360 / sides`).

**Math Connection:** Polygons, angles (interior and exterior angles), division.

**PictoBlox Blocks:**
- `when green flag clicked`
- `set [sides] to [pick random 3 to 8]` (Random Number)
- `set [angle] to [360 / sides]`
- `repeat [sides]` (Loop)
  - `move forward [50] steps`
  - `turn right [angle] degrees`


## Project 5: Treasure Hunt with Random Obstacles

**Concepts:** Random Number Generation, Conditional Statements, Boolean Logic, Input, Output

**Objective:** Wizbot navigates a grid to find treasure, with random obstacles appearing each time.

**Description:** Generate random positions for obstacles. The user inputs a direction (forward/left/right). The program checks if the chosen path has an obstacle using conditional statements. If clear, Wizbot moves; if blocked, it beeps and stays.

**Math Connection:** Grid coordinates, probability, logical reasoning.

**PictoBlox Blocks:**
- `when green flag clicked`
- `set [obstacle] to [pick random 1 to 6]` (Random obstacle position)
- `ask [Move forward? (yes/no)] and wait`
- `if [answer = yes] and [position ≠ obstacle] then` (Boolean Logic + Comparison)
  - `move forward [1] cell`
- `else`
  - `play sound [beep]`


## Project 6: Counting Steps Counter

**Concepts:** Counters, Loops, Variables, Output

**Objective:** Wizbot counts and displays how many steps it takes to reach a target.

**Description:** Set a target distance. Wizbot moves forward one step at a time while a counter variable increases. The loop continues until the counter equals the target. Display the final count.

**Math Connection:** Counting, number sequences, addition.

**PictoBlox Blocks:**
- `when green flag clicked`
- `set [counter] to [0]`
- `set [target] to [10]`
- `repeat until [counter = target]`
  - `move forward [1] step`
  - `change [counter] by [1]`
- `say [counter]` (Output)


## Project 7: Comparison Maze Runner

**Concepts:** Comparison Operators, Conditional Statements, Variables, Input, Output

**Objective:** Wizbot chooses the correct path by comparing two numbers.

**Description:** Two random numbers are generated. The user predicts which is larger. If correct, Wizbot takes the "correct" path (forward); if wrong, it takes the "wrong" path (backward).

**Math Connection:** Comparing numbers (greater than, less than), inequalities.

**PictoBlox Blocks:**
- `when green flag clicked`
- `set [num1] to [pick random 1 to 20]`
- `set [num2] to [pick random 1 to 20]`
- `ask [Which number is larger? (1 or 2)] and wait`
- `if [num1 > num2] and [answer = 1] then` (Comparison + Boolean Logic)
  - `move forward [5] steps`
- `else if [num2 > num1] and [answer = 2] then`
  - `move forward [5] steps`
- `else`
  - `move backward [3] steps`


## Project 8: Pattern Generator with Modulus

**Concepts:** Modulus Operator (%), Loops, Variables, Output

**Objective:** Wizbot creates alternating patterns (e.g., zigzag) based on whether the step number is even or odd.

**Description:** Use a loop from 1 to 10. For each iteration, check if the loop counter is even or odd using modulus. If even, turn right; if odd, turn left. This creates a zigzag pattern.

**Math Connection:** Even/odd patterns, sequences, remainders.

**PictoBlox Blocks:**
- `when green flag clicked`
- `repeat [10]`
  - `if [counter % 2 = 0] then`
    - `turn right [45] degrees`
  - `else`
    - `turn left [45] degrees`
  - `move forward [30] steps`
  - `change [counter] by [1]`


## Project 9: Button-Controlled Robot

**Concepts:** Events, Input, Output, Conditional Statements

**Objective:** Wizbot responds differently to different button presses.

**Description:** Using PictoBlox's event blocks, program Wizbot to respond to keyboard events. Pressing the up arrow makes it move forward, down arrow makes it go backward, left arrow turns left, and right arrow turns right.

**Math Connection:** Direction and spatial awareness, coordinate geometry.

**PictoBlox Blocks:**
- `when [up arrow] key pressed` (Events)
  - `move forward [2] steps`
- `when [down arrow] key pressed`
  - `move backward [2] steps`
- `when [left arrow] key pressed`
  - `turn left [15] degrees`
- `when [right arrow] key pressed`
  - `turn right [15] degrees`


## Project 10: Boolean Logic Gate Challenge

**Concepts:** Boolean Logic, Conditional Statements, Variables, Input, Output

**Objective:** Wizbot moves only when TWO conditions are true (AND logic) or when EITHER condition is true (OR logic).

**Description:** Create two conditions—e.g., "is it daytime?" and "is the path clear?". Using Boolean AND/OR, determine if Wizbot should move. Students learn how logical operators combine conditions.

**Math Connection:** Truth tables, logical reasoning, set theory basics.

**PictoBlox Blocks:**
- `when green flag clicked`
- `ask [Is it daytime? (yes/no)] and wait`
- `set [daytime] to [answer = yes]`
- `ask [Is path clear? (yes/no)] and wait`
- `set [clear] to [answer = yes]`
- `if [daytime and clear] then` (Boolean AND Logic)
  - `move forward [5] steps`
  - `say [Moving forward!]` (Output)
- `else`
  - `say [Cannot move!]`


## Summary Table

| Project | Variables | Random | If-Else | Modulus | Comparison | Events | Input | Output | Loops | Counters | Boolean |
|---------|-----------|--------|---------|---------|------------|--------|-------|--------|-------|----------|---------|
| 1. Number Line Jumps | ✓ | | | | | ✓ | | ✓ | ✓ | | |
| 2. Multiplication Dance | ✓ | | | | | ✓ | | ✓ | ✓ | ✓ | |
| 3. Even-Odd Path | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ | | | | |
| 4. Random Shape | ✓ | ✓ | | | | ✓ | | ✓ | ✓ | | |
| 5. Treasure Hunt | ✓ | ✓ | ✓ | | | ✓ | ✓ | ✓ | | | ✓ |
| 6. Counting Steps | ✓ | | | | | ✓ | | ✓ | ✓ | ✓ | |
| 7. Comparison Maze | ✓ | ✓ | ✓ | | ✓ | ✓ | ✓ | ✓ | | | ✓ |
| 8. Pattern Generator | ✓ | | ✓ | ✓ | | ✓ | | ✓ | ✓ | ✓ | |
| 9. Button Robot | | | ✓ | | | ✓ | ✓ | ✓ | | | |
| 10. Boolean Logic | ✓ | | ✓ | | | ✓ | ✓ | ✓ | | | ✓ |

---

**Note:** Wizbot Maxx supports PictoBlox Junior Blocks for block-based coding. All projects above can be implemented using the Wizbot Advance Blocks extension in PictoBlox. For screen-free button-based versions, simplify the projects to use Wizbot's physical buttons for input and movement commands.
