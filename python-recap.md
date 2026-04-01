# Complete Python & AI Master Recap

---

## Part 1: Python Programming Basics

### 1.1 What is Coding?
- **Coding** = writing instructions for machines to perform tasks
- **Algorithmic thinking** = breaking problems into step-by-step solutions (algorithms)

### 1.2 Python Overview
- Simple, powerful programming language
- Used in: AI, web development, automation, data science
- **Modes**: Interactive (one command at a time) | Script (multi-line programs)

### 1.3 Basic Functions
```python
print("Hello")      # displays output
input("Enter: ")    # takes user input
```

### 1.4 Comments
```python
# Single-line comment
""" Multi-line comment """
```

### 1.5 Variables & Constants
| Type | Description | Example |
|------|-------------|---------|
| **Variable** | Value can change | `age = 25` |
| **Constant** | Fixed value (uppercase) | `PI = 3.14` |

### 1.6 Data Types & Typecasting

| Data Type | Example |
|-----------|---------|
| `int` | `42` |
| `float` | `3.14` |
| `str` | `"Hello"` |
| `bool` | `True / False` |
| `list` | `[1, 2, 3]` |
| `tuple` | `(1, 2, 3)` (immutable) |

```python
# Typecasting
int("123")      # string → integer
float(5)        # integer → float
str(123)        # integer → string
```

### 1.7 Lists
```python
fruits = ["apple", "banana", "cherry"]

# Indexing: 0 = first, -1 = last
print(fruits[0])    # apple
print(fruits[-1])   # cherry

# Methods
fruits.append("orange")   # add to end
fruits.remove("banana")   # remove item
fruits.sort()             # sort ascending
fruits.reverse()          # reverse order
```

### 1.8 Operators

| Type | Operators |
|------|----------|
| **Arithmetic** | `+`, `-`, `*`, `/`, `%` |
| **Assignment** | `=`, `+=`, `-=`, `*=`, `/=` |
| **Relational** | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| **Logical** | `and`, `or`, `not` |

### 1.9 Conditional Statements
```python
# if statement
if age >= 18:
    print("Adult")

# if-else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# if-elif-else
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

# Nested conditionals
if age >= 18:
    if has_license:
        print("Can drive")
```

### 1.10 Loops
```python
# For loop - iterates over sequence
for fruit in fruits:
    print(fruit)

for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

# While loop - runs until condition false
count = 0
while count < 5:
    print(count)
    count += 1
```

### 1.11 Python Libraries

| Library | Purpose |
|---------|---------|
| **NumPy** | Numerical operations, arrays |
| **Pandas** | Data handling and analysis |
| **Matplotlib** | Data visualization |
| **OpenCV** | Image processing |

### 1.12 Tools
- **Jupyter Notebook** = interactive Python environment
- **Virtual environments** = isolate project dependencies

---

## Part 2: AI & Machine Learning Fundamentals

### 2.1 Core Concepts
| Concept | Description |
|---------|-------------|
| **AI** | Uses data to learn patterns and make predictions |
| **Features** | Characteristics that help classify objects |
| **Labels** | Correct answers AI learns to predict |
| **Training Data** | Used for learning patterns |
| **Testing Data** | Used to check accuracy |

### 2.2 AI Approaches

| Approach | Description |
|----------|-------------|
| **Rule-Based** | Follows fixed rules, cannot improve |
| **Learning-Based** | Learns from data, improves with experience |

### 2.3 Types of Machine Learning

| Type | Description | Examples |
|------|-------------|---------|
| **Supervised Learning** | Uses labeled data | Classification, Regression |
| **Unsupervised Learning** | Finds patterns in unlabeled data | Clustering, Association |
| **Reinforcement Learning** | Trial and error with rewards/penalties | Game AI, Robotics |

### 2.4 Deep Learning
- Processes large datasets and recognizes complex patterns
- **Artificial Neural Networks (ANNs)** = mimic human brain structure

### 2.5 Neural Network Components

| Component | Function |
|-----------|----------|
| **Input Layer** | Receives raw data |
| **Hidden Layers** | Process and transform data |
| **Weights & Biases** | Adjust feature importance |
| **Activation Function** | Filters unnecessary details |
| **Perceptron** | Combines inputs, weights, bias with threshold |

### 2.6 Convolutional Neural Networks (CNNs)
- Specialize in image processing
- Used in facial recognition and object detection

| CNN Layer | Function |
|-----------|----------|
| **Convolution Layer** | Detects features using filters/kernels |
| **ReLU Layer** | Removes negative values |
| **Pooling Layer** | Reduces size, retains important features |
| **Fully Connected Layer** | Classifies the image |

---

## Part 3: Natural Language Processing (NLP)

### 3.1 What is NLP?
- Branch of AI enabling computers to understand, interpret, and respond to human language
- **Natural language** = how humans communicate
- **Processing** = analyzing language for machines

### 3.2 Five Stages of NLP

| Stage | Function |
|-------|----------|
| **Lexical Analysis** | Breaks text into words/phrases |
| **Syntactic Analysis** | Checks grammar structure |
| **Semantic Analysis** | Understands meaning |
| **Discourse Integration** | Understands context across sentences |
| **Pragmatic Analysis** | Interprets intent/purpose |

### 3.3 Text Processing Steps
| Step | Description |
|------|-------------|
| **Sentence Segmentation** | Split text into sentences |
| **Tokenization** | Split sentences into words/tokens |
| **Stop Word Removal** | Remove common words (the, is, and) |
| **Case Conversion** | Convert all to lowercase |

### 3.4 Word Reduction

| Technique | Description |
|-----------|-------------|
| **Stemming** | Reduces to root form (may lose meaning) |
| **Lemmatization** | Reduces to base form (preserves meaning) |

### 3.5 Converting Text to Numbers

| Method | Description |
|--------|-------------|
| **Bag of Words (BoW)** | Counts word frequencies in documents |
| **TF-IDF** | Gives importance to unique/meaningful words |

### 3.6 NLP Tools
| Code-Based | No-Code |
|------------|--------|
| NLTK | MonkeyLearn |
| SpaCy | Orange Data Mining |

### 3.7 NLP Applications & Chatbots
- **Chatbots**: Script Bots (rule-based) | Smart Bots (AI-powered)
- Voice assistants, auto-generated captions, language translation, sentiment analysis, keyword extraction

---

## Part 4: Computer Vision (CV)

### 4.1 What is Computer Vision?
- Enables machines to see, analyze, and understand images and videos
- Mimics human vision: capturing, processing, recognizing visual data

### 4.2 Image Basics

| Concept | Description |
|---------|-------------|
| **Pixel** | Smallest unit of an image |
| **Resolution** | Higher = clearer images |
| **Grayscale** | 0 (black) to 255 (white) |
| **RGB** | Red, Green, Blue channels combine for color |

### 4.3 Key CV Tasks
1. **Image Classification** – What is in the image?
2. **Object Detection** – Where are objects located?
3. **Instance Segmentation** – Pixel-level object boundaries

### 4.4 Feature Extraction
- Detects edges, corners, and patterns in images
- **Convolution** = uses small filters (kernels) to highlight important features

### 4.5 CV Applications
- Facial recognition
- Medical imaging
- Self-driving cars
- AR filters (Snapchat, Instagram)

---

## Part 5: Statistics for AI

### 5.1 Statistical Concepts

| Concept | Description |
|---------|-------------|
| **Statistical Sampling** | Selecting representative subset of population |
| **Mean** | Average value |
| **Median** | Middle value |
| **Mode** | Most frequent value |

### 5.2 Data Distribution

| Type | Description |
|------|-------------|
| **Normal Distribution** | Bell curve, symmetric |
| **Left-Skewed** | Tail extends to left |
| **Right-Skewed** | Tail extends to right |

### 5.3 Variability & Probability

| Concept | Description |
|---------|-------------|
| **Probability** | Likelihood of events based on past data |
| **Variance** | Measures spread of data from mean |
| **Standard Deviation** | Square root of variance, indicates consistency |
| **Outliers** | Extreme values that differ significantly |

### 5.4 AI Development Approaches

| Approach | Description |
|----------|-------------|
| **High-Code** | Full programming control and flexibility |
| **Low-Code** | Minimal coding with visual tools |
| **No-Code** | No programming required, drag-and-drop |

### 5.5 No-Code AI Tools
- **Orange Data Mining** = visual data analysis through drag-and-drop widgets

### 5.6 Statistics Applications
- Weather forecasts
- YouTube recommendations
- Online shopping suggestions
- Internet search
- Targeted advertising
- Genomics

---

## Part 6: Model Evaluation

### 6.1 Why Evaluate?
Ensures AI models are accurate, reliable, and perform well before deployment

### 6.2 Train-Test Split

| Dataset | Purpose |
|---------|---------|
| **Training Data** | Model learns patterns |
| **Testing Data** | Model evaluation |

- Prevents **overfitting** (model memorizes instead of learning patterns)

### 6.3 Accuracy Metrics

| Metric | Description |
|--------|-------------|
| **Accuracy** | Percentage of correct predictions |
| **Error** | Difference between predicted and actual results |
| **Absolute Error** | \|Predicted - Actual\| |
| **Error Rate** | Errors / Total predictions |

### 6.4 Confusion Matrix

| | Predicted Positive | Predicted Negative |
|---|-------------------|-------------------|
| **Actual Positive** | **True Positive (TP)** | **False Negative (FN)** |
| **Actual Negative** | **False Positive (FP)** | **True Negative (TN)** |

### 6.5 Classification Metrics

| Metric | Formula | What It Measures |
|--------|--------|------------------|
| **Accuracy** | (TP + TN) / Total | Overall correctness |
| **Precision** | TP / (TP + FP) | How many predicted positives are actually correct |
| **Recall** | TP / (TP + FN) | How well model identifies actual positives |
| **F1 Score** | 2 × (P × R) / (P + R) | Balance of precision and recall (for unbalanced datasets) |

### 6.6 Ethical Concerns in AI
| Concern | Description |
|---------|-------------|
| **Bias** | Unfair discrimination in AI decisions |
| **Transparency** | Understanding how decisions are made |
| **Accountability** | Responsibility for AI outcomes |

---

## Part 7: Complete Quick Reference

### Python
```python
# Variables & Data Types
name = "Alice"          # string
age = 25                # int
price = 19.99           # float
is_valid = True         # bool
colors = ["red", "blue"] # list

# Conditionals
if condition:
    pass
elif condition:
    pass
else:
    pass

# Loops
for item in list:
    print(item)

while condition:
    # code
```

### AI/ML Flow
```
Data → Training → Model → Testing → Evaluation → Deployment
```

### NLP Pipeline
```
Raw Text → Tokenization → Stop Word Removal → Stemming/Lemmatization → Feature Extraction → Analysis
```

### CV Pipeline
```
Image → Pixels → Feature Extraction → Convolution → CNN → Classification
```

### Evaluation Metrics
```
Confusion Matrix → Precision → Recall → F1 Score → Accuracy
```

---

## Summary Table

| Domain | Key Concepts |
|--------|-------------|
| **Python** | print(), input(), variables, loops, conditionals, lists, tuples, libraries |
| **AI/ML** | Supervised, Unsupervised, Reinforcement, features, labels, training/testing |
| **Deep Learning** | ANNs, CNNs, layers, weights, activation functions, perceptron |
| **NLP** | Tokenization, stop words, stemming, lemmatization, BoW, TF-IDF |
| **CV** | Pixels, RGB, grayscale, convolution, feature extraction |
| **Statistics** | Mean, median, mode, variance, distribution, outliers, sampling |
| **Evaluation** | Train-test split, confusion matrix, precision, recall, F1, accuracy |
| **Ethics** | Bias, transparency, accountability |

---
