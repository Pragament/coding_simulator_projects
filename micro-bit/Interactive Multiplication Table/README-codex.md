# Interactive Multiplication Table using micro:bit

## Project Summary
- Concept: Number patterns, multiples, integers
- Project: Press buttons to scroll through a multiplication table; shake to switch between positive and negative integers
- Components: micro:bit + virtual display
- Math Link: Number operations, patterns
- Simulate: Basic counter with +/- (modify for tables)

## List of Materials Required
- micro:bit (physical device or Tinkercad simulator)
- micro:bit 5x5 LED display (built-in)
- Button A and Button B (built-in)
- Accelerometer (built-in, used for shake)
- Computer with internet access (for Tinkercad)

## How to Build
### Introduction
This project turns the micro:bit into an interactive multiplication table explorer. Button presses step through multiples of a fixed number, and a shake gesture flips the sign to demonstrate positive and negative integers.

### Working Principle
- `N` is the table number (e.g., 5)
- `k` is the current multiplier (1 to 10)
- `sign` toggles between `1` and `-1`
- Displayed value = `N * k * sign`

Controls:
- Button B: increment `k`
- Button A: decrement `k`
- Shake: flip `sign`

## Detailed Guidelines
### DIY Tutorial Guide
You can build this in Tinkercad Circuits or on a real micro:bit. No extra wiring is required because buttons, display, and accelerometer are built in.

### Procedure Steps
1. Create a new micro:bit circuit in Tinkercad.
2. Open the Code editor and select Blocks (or MicroPython).
3. Create variables `N`, `k`, and `sign`.
4. On start:
   - Set `N = 5`
   - Set `k = 1`
   - Set `sign = 1`
   - Show `N * k * sign`
5. On Button B pressed:
   - Increase `k` by 1
   - If `k > 10`, set `k = 1`
   - Show `N * k * sign`
6. On Button A pressed:
   - Decrease `k` by 1
   - If `k < 1`, set `k = 10`
   - Show `N * k * sign`
7. On shake:
   - Set `sign = sign * -1`
   - Show `N * k * sign`
8. Start the simulation or flash the device.

### How It Works
- The multiplier `k` cycles through 1 to 10, letting you explore a full table.
- The shake gesture multiplies by `-1`, making the same table negative to reinforce integer concepts.
- The display updates after every input event so the learner sees immediate feedback.

### Tips
- Change `N` to explore different tables (e.g., 2, 3, 7, 9, 12).
- For larger results that exceed the 5x5 display quickly, reduce `N` or keep `k` small.
- Use consistent step sizes to help identify number patterns.

### Testing
- Press Button B ten times and verify it wraps from 10 back to 1.
- Press Button A from 1 and verify it wraps to 10.
- Shake twice and confirm the sign returns to positive.
- Try `N = 5` and verify the displayed values: 5, 10, 15, 20, ...

## Troubleshooting Guide
- Issue: Display does not change when pressing buttons.
  - Possible causes: Button handlers not connected, or logic not inside event blocks.
  - Solution: Confirm code is inside the correct `on button A/B pressed` blocks and that `show number` is called.

- Issue: The sign never changes.
  - Possible causes: Shake event not used or `sign` not multiplied by `-1`.
  - Solution: Use the `on shake` event and set `sign = sign * -1`.

- Issue: Results jump or skip values.
  - Possible causes: `k` is updated in multiple places or wrapped incorrectly.
  - Solution: Update `k` only in the button events and ensure wrap limits are 1 and 10.

- Issue: Unexpected negative values after startup.
  - Possible causes: `sign` not initialized.
  - Solution: Set `sign = 1` in the on start block.

- Issue: Output seems wrong for the table.
  - Possible causes: `N` not set to intended value.
  - Solution: Verify `N` is assigned the correct table number on start.
