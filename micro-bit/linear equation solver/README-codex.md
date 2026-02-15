# Linear Equation Solver using micro:bit

## Project Summary
- Concept: `ax + b = c` equations
- Project: Input `a`, `b`, `c` using buttons and solve for `x`
- Code: `x = (c - b) / a`
- Math Link: Algebra, solving equations
- Simulate: Variable manipulator (create your own)

## List of Materials Required
- micro:bit (physical device or Tinkercad simulator)
- micro:bit 5x5 LED display (built-in)
- Button A and Button B (built-in)
- Accelerometer (built-in, used for shake)
- Computer with internet access (for Tinkercad)

## How to Build
### Introduction
This project turns the micro:bit into a simple algebra solver. You enter the coefficients for a linear equation `ax + b = c`, then the device calculates and displays the solution for `x`.

### Working Principle
- `a`, `b`, `c` are entered one at a time using buttons
- A `state` variable controls which value is currently being edited
- Shake advances to the next value or triggers the solve step
- Displayed value = `(c - b) / a` when solving

Controls:
- Button B: increase current value
- Button A: decrease current value
- Shake: move to next step (a -> b -> c -> solve)

## Detailed Guidelines
### DIY Tutorial Guide
Build the circuit in Tinkercad Circuits or on a real micro:bit. No extra wiring is required because the micro:bit already has buttons, a display, and an accelerometer.

### Procedure Steps
1. Create a new micro:bit circuit in Tinkercad.
2. Open the Code editor and select Blocks (or MicroPython).
3. Create variables `a`, `b`, `c`, and `state`.
4. On start:
   - Set `a = 1`, `b = 0`, `c = 0`
   - Set `state = 0`
   - Show which variable is active (optional: show string `a`, `b`, `c`)
5. Button B pressed:
   - If `state = 0`, increase `a`
   - If `state = 1`, increase `b`
   - If `state = 2`, increase `c`
6. Button A pressed:
   - If `state = 0`, decrease `a`
   - If `state = 1`, decrease `b`
   - If `state = 2`, decrease `c`
7. Add wrap limits (example: keep values between `-9` and `10`).
8. On shake:
   - If `state < 3`, increase `state` by 1
   - If `state = 3`, solve and display `x`
9. If `a = 0`, display `Err` to avoid division by zero.
10. Start the simulation or flash the device.

### How It Works
- You edit one variable at a time, controlled by `state`.
- The solver uses the formula `x = (c - b) / a`.
- The display updates after every input so learners see the equation change.

### Tips
- Use small integer ranges to keep values readable on the 5x5 display.
- Add a short delay after showing a label (like `a`, `b`, `c`) so it is visible.
- If you want only integer results, choose values where `c - b` is divisible by `a`.

### Testing
- Set `a = 2`, `b = 3`, `c = 7` and confirm `x = 2`.
- Set `a = 1`, `b = 0`, `c = 5` and confirm `x = 5`.
- Set `a = 0` and confirm the display shows `Err`.
- Cycle through states and confirm the correct variable is being edited.

## Troubleshooting Guide
- Issue: Buttons change the wrong variable.
  - Possible causes: `state` checks are incorrect or missing.
  - Solution: Verify `if/else` blocks map `state` to the correct variable.

- Issue: The result is not shown after shake.
  - Possible causes: `state` never reaches the solve step.
  - Solution: Ensure shake increases `state` and that `state = 3` runs the solve logic.

- Issue: Display shows `Err` unexpectedly.
  - Possible causes: `a` is zero.
  - Solution: Increase `a` to a non-zero value before solving.

- Issue: Results are decimals or hard to read.
  - Possible causes: `(c - b)` is not divisible by `a`.
  - Solution: Use values that produce integer results or round the output.

- Issue: Value jumps beyond the intended range.
  - Possible causes: Wrap logic is missing or incorrect.
  - Solution: Add bounds (example: `-9` to `10`) and wrap when exceeded.
