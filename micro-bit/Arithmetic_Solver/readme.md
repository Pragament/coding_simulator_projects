


# 📟 Arithmetic Progression Generator (Micro:bit)

## 📌 Project Overview

This project implements an **Arithmetic Progression (AP) Generator** using the **BBC Micro:bit** and **MakeCode Blocks**.

It allows users to:

* Generate AP terms
* Display current term
* Increment or decrement term index
* Compute the sum formula component dynamically

The project demonstrates understanding of:

* Variables
* Mathematical formulas (AP concepts)
* Event-driven programming
* Micro:bit button controls
* Continuous looping (`forever` block)

---

## 🧮 Mathematical Concept Used

An Arithmetic Progression (AP) follows:

[
T_n = a + (n-1)d
]

Where:

* `a` = First term
* `d` = Common difference
* `n` = Term number
* `Tn` = nth term

The sum formula components used:

[
\frac{n}{2}, \quad 2a, \quad d(n-1)
]

---

## ⚙️ Initial Values

When the program starts:

| Variable | Value | Meaning           |
| -------- | ----- | ----------------- |
| a        | 1     | First term        |
| d        | 4     | Common difference |
| n        | 1     | Term position     |

The first term is displayed on startup.

---

## 🔄 Program Logic

### 🔹 On Start

* Sets:

  * `a = 1`
  * `d = 4`
  * `n = 1`
* Displays the first term (`a`)

---

### 🔹 Forever Loop

Continuously calculates:

* `t1 = n / 2`
* `t2 = 2 × a`
* `t3 = d × (n - 1)`
* Displays:

  ```
  t1 × (t2 + t3)
  ```

This represents the AP formula component structure.

---

## 🎮 Button Controls

### 🔵 Button B (Next Term)

* Displays current term:

  ```
  a + n × d
  ```
* Increments:

  ```
  n = n + 1
  ```

➡ Moves forward in the progression.

---

### 🔴 Button A (Previous Term)

* Displays current term:

  ```
  a + n × d
  ```
* Decrements:

  ```
  n = n - 1
  ```

➡ Moves backward in the progression.

---

## 📊 Example Output (Given a = 1, d = 4)

Arithmetic Progression:

```
1, 5, 9, 13, 17, ...
```

If:

* n = 1 → Output: 1
* n = 2 → Output: 5
* n = 3 → Output: 9
* n = 4 → Output: 13

---

## 🛠️ Technologies Used

* BBC Micro:bit
* Microsoft MakeCode (Block Programming)
* Event-driven embedded programming
* Basic mathematical modeling

---

## 🎯 Learning Outcomes

This project helps understand:

* Arithmetic progression formulas
* Variable manipulation
* Button-based event handling
* Continuous calculations using loops
* Embedded system logic
* Mathematical visualization on hardware

---

## 🚀 Future Improvements

* Add reset functionality
* Add limit check (prevent negative n)
* Display full AP sequence automatically
* Convert to JavaScript version in MakeCode
* Build web-based AP simulator

---

## 📂 How to Run

1. Open **Microsoft MakeCode**
2. Select **Micro:bit**
3. Recreate blocks as shown
4. Download `.hex` file
5. Flash to Micro:bit
6. Use buttons A & B to navigate AP terms

---

## 👨‍💻 Author

Developed as part of learning mathematical modeling and embedded programming using Micro:bit.

---

## 🧩 Block Programming Design

![Block Design](images/Screenshot%202026-02-24%20105808.png)
![Block Design](images/Screenshot%202026-02-24%20105816.png)
![Block Design](images/Screenshot%202026-02-24%20111715.png)

