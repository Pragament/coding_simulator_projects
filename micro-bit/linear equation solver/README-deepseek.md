# 🎯 **Algebra Wizard: The micro:bit Equation Solver** 🎯

## 📖 **The Magical Math Quest**

Welcome, Algebra Apprentice! You're about to embark on an enchanted journey where you'll create your very own pocket-sized equation solver. With three mystical numbers and a wave of your wand (okay, a shake of your micro:bit), you'll conjure up the secret value of `x` that makes equations come true!

---

## 🌟 **Your Magical Mission**

- **Master the Magic Formula**: `ax + b = c` – three numbers hold the key to finding `x`!
- **Become a Number Wizard**: Input your own coefficients and watch the solution appear
- **Discover the Power of Algebra**: See how changing one number transforms everything

---

## 🧙‍♂️ **The Sorcerer's Toolkit**

| Tool | What It Does |
|------|--------------|
| **micro:bit** | Your magical calculator (real or Tinkercad version) |
| **5x5 Light Grid** | The crystal ball where answers appear |
| **Button A & B** | Your magic wands – increase or decrease numbers |
| **Shake Sensor** | Your spell-casting motion to move forward |
| **Computer** | Your workshop entrance (for Tinkercad) |

---

## 🔮 **How the Magic Works**

### The Enchantment Formula 🪄

Every linear equation hides a secret number `x`. To find it, we follow this spell:

**The Spell:** `x = (c - b) ÷ a`

Where:
- `a` is the multiplier (the number that multiplies `x`)
- `b` is the adder (the number added to `ax`)
- `c` is the total (what it all equals)

**Think About It:** If `a = 2`, `b = 3`, and `c = 7`, the equation is `2x + 3 = 7`. What number for `x` makes this true? Try it in your head first!

### Your Magical Controls 🎮

| Action | What Happens | Try Chanting |
|--------|--------------|--------------|
| Press Button B | Increase current number | "Grow, number, grow!" |
| Press Button A | Decrease current number | "Shrink, number, shrink!" |
| Shake | Move to next number or solve | "Onward, magic, onward!" |

---

## 🏰 **Build Your Algebra Wizard – Step by Step**

### Step 1: Enter the Enchanted Workshop 🚪
Open Tinkercad Circuits and create a new micro:bit project. You're now in your magic lab!

### Step 2: Prepare Your Spell Ingredients 📦
Create four magic containers (variables):
- `a` = The multiplier (starts at 1)
- `b` = The adder (starts at 0)
- `c` = The total (starts at 0)
- `state` = Your stage marker (tracks where you are: 0=a, 1=b, 2=c, 3=solve)

### Step 3: Cast the Opening Spell 🌅
```
On Start:
    Set a = 1
    Set b = 0
    Set c = 0
    Set state = 0
    Show "a" on screen (so you know it's time to set a!)
```

### Step 4: Create Your Number-Adjusting Wands ✨

**For Button B (Increase Magic):**
```
On Button B Pressed:
    If state is 0, add 1 to a
    If state is 1, add 1 to b
    If state is 2, add 1 to c
    Show the new value on screen
```

**For Button A (Decrease Magic):**
```
On Button A Pressed:
    If state is 0, subtract 1 from a
    If state is 1, subtract 1 from b
    If state is 2, subtract 1 from c
    Show the new value on screen
```

### Step 5: Add the Number Wrapping Charm 🔄
Keep numbers friendly for your 5x5 display:
```
When adding to a number:
    If it becomes greater than 10, set it back to -9
When subtracting from a number:
    If it becomes less than -9, set it to 10
```

**Why -9 to 10?** This range fits nicely on the micro:bit display and gives you plenty of numbers to explore!

### Step 6: Cast the Shake-to-Progress Spell 🎲
```
On Shake:
    If state is less than 3:
        Add 1 to state
        If state is 0, show "a"
        If state is 1, show "b"
        If state is 2, show "c"
    Otherwise (state is 3):
        If a equals 0:
            Show "Err" (can't divide by zero!)
        Else:
            Calculate x = (c - b) ÷ a
            Show x on screen
```

---

## 🎨 **Fun Activities & Challenges**

### 🎭 **Hands-On Game: Equation Detective**
1. Have a friend secretly choose an equation (like `3x + 2 = 11`)
2. Without telling you the equation, they set `a=3`, `b=2`, `c=11`
3. Watch the micro:bit reveal the secret `x`!
4. Can you guess the original equation from the numbers?

### 🖍️ **Drawing Prompt: The Equation Balance**
Draw a magical balance scale:
- On the left side, draw `a` boxes labeled `x` plus `b` gems
- On the right side, draw `c` gems
- Show how finding `x` is like making both sides equal

### 🧩 **Pattern Detective Game**
Try these equations and look for patterns:
- `2x + 0 = 10` → `x = ?`
- `2x + 2 = 10` → `x = ?`
- `2x + 4 = 10` → `x = ?`

**What do you notice?** How does changing `b` affect `x`?

### 🎪 **The Great Number Hunt**
Find real things that match your equations:
- If `x` is the number of apples in each bag, `a` is bags, `b` is loose apples, and `c` is total apples...
- Create a story for `3x + 2 = 11` about sharing snacks!

---

## 💡 **Memory Tricks & Shortcuts**

**The Equation Song** 🎵
(Sing to "Twinkle, Twinkle, Little Star")

*"ax plus b equals c,*
*Find the x, just wait and see!*
*Take the c and minus b,*
*Divide by a – that's the key!*
*Now you know just what to do,*
*Algebra is great, it's true!"*

**The "BAC" Memory Helper** 🥪
Think of a BACON sandwich:
- **B** comes first? No – in `(c - b) ÷ a`, we actually do **C - B** first!
- Remember: "**C**ats **B**ehave **A**wfully" – do **C** minus **B** first, then divide by **A**

**Finger Math** ✋
Hold up fingers for each step:
1 finger: `c - b`
2 fingers: divide by `a`
3 fingers: `x` appears!

---

## 🌍 **Real-World Adventures**

**Shopping Spree** 🛍️
Imagine: `3x + 2 = 11`
- You buy 3 identical toys (`3x`)
- Plus you get 2 free stickers (`+ 2`)
- You pay for 11 items total (`= 11`)
- Each toy package has `x` items inside!

**Recipe Magic** 👩‍🍳
`2x + 1 = 9`
- A cookie recipe needs 2 cups of flour per batch (`2x`)
- Plus 1 extra cup for sprinkling (`+ 1`)
- You have 9 cups total (`= 9`)
- How many batches can you make? (`x = 4` batches!)

**Journey Planning** 🗺️
`4x + 3 = 19`
- You drive 4 hours each day (`4x`)
- Plus you already drove 3 hours yesterday (`+ 3`)
- Total trip is 19 hours (`= 19`)
- How many more days? (`x = 4` days!)

**Allowance Algebra** 💰
`5x - 2 = 13` (Wait, minus? That's just `b = -2`!)
- You get $5 each week for `x` weeks
- You spent $2 on candy
- You have $13 left
- How many weeks? (`x = 3` weeks!)

---

## 🔍 **Talk to a Friend**

**Equation Explorers Discussion:**

1. "What happens to `x` when `a` gets bigger? When `b` gets bigger?"
2. "Can you create an equation where `x` is a negative number? What would that mean in real life?"
3. "Why can't we divide by zero? What would happen if `a = 0` in our solver?"
4. "If you could add a fourth variable to our equation, what would it do?"
5. "What's the strangest equation you can make that still gives a whole number for `x`?"

---

## 🛠️ **Fix-It Guide (When Spells Go Wrong)**

**Problem:** Buttons change the wrong number!
**Fix-it Charm:** Check your `state` tracker – is it pointing to the right variable? Add a quick "show state" to debug!

**Problem:** The shake spell won't solve!
**Fix-it Charm:** Make sure `state` actually reaches 3. Try adding "show state" after each shake to see where you are.

**Problem:** "Err" appears and won't go away!
**Fix-it Charm:** Check if `a` is zero. Press Button B while in `a`-editing mode to increase it above zero.

**Problem:** Answers are messy decimals!
**Fix-it Charm:** Choose numbers where `(c - b)` divides evenly by `a`. Try `a=2`, `b=4`, `c=10` – perfect!

**Problem:** Numbers disappear off the screen!
**Fix-it Charm:** Remember the 5x5 display can only show one or two digits. Keep numbers between -9 and 99.

**Problem:** I forgot which variable I'm editing!
**Fix-it Charm:** Add a quick flash of `a`, `b`, or `c` before showing each number. Or use different symbols!

---

## 🚀 **Level Up Challenges**

**Beginner Wizard:** Create and solve 5 different equations that all give `x = 3`. What patterns do you notice?

**Intermediate Wizard:** Modify your code to show the full equation before solving, like `2x + 3 = 7` scrolling across!

**Advanced Wizard:** Add a "random equation" mode – when you press both buttons, it generates random `a`, `b`, and `c` for you to solve!

**Master Wizard:** Create a two-step verification – after showing `x`, shake again to check your work by calculating `a × x + b` and comparing to `c`!

**Grand Sorcerer:** Add a fraction mode! If `(c - b)` doesn't divide evenly by `a`, show the answer as a simplified fraction like `3/2` instead of `1.5`

---

## 📓 **Your Algebra Adventure Journal**

Create a wizard's journal and record:

| Date | My Equation | My `x` | Story Behind It |
|------|-------------|--------|-----------------|
| | `2x + 3 = 11` | 4 | 2 bags with x apples + 3 loose = 11 total |
| | `5x - 2 = 13` | 3 | 5 weeks of $x - $2 spent = $13 saved |
| | | | |

**Draw a Picture:** Illustrate one of your equations as a real-life situation

**Wonder Corner:** Write down three questions you still have about algebra

**Prediction Practice:** Before solving, always guess what `x` might be. Were you close?

---

## 🎉 **Celebrate Your Wizardry!**

You've done it! You've built a magical device that can solve any linear equation you throw at it. You're no longer just learning algebra – you're **living** it!

Remember these magical truths:
- **Every number tells a story**
- **Every equation has a secret waiting to be discovered**
- **YOU have the power to find it**

Now go forth, Algebra Wizard, and solve the mysteries of the mathematical universe! 🧙‍♂️✨

---

**Bonus Spell:** Try this challenge equation and see if your solver works:
`-3x + 7 = -2` (Hint: What's `x`?)

*Whisper: The answer is 3! Did you get it?* 🤫