# 🧬 Bioinformatics + AI Workshop (with Biopython)

Focus: Python + Biopython + Machine Learning

---

## 🟢 WEEK 1: Python Basics (Foundation)

### Topics:
- Variables, strings, lists
- Loops & conditions
- DNA as strings

### Example:
```python
dna = "ATGCGCTA"
print("Length:", len(dna))
print("GC Content:", (dna.count("G")+dna.count("C"))/len(dna)*100)
```

---

## 🟢 WEEK 2: Introduction to Biopython

### Topics:
- What is Biopython
- Sequence objects
- Basic sequence operations

### Install:
```bash
pip install biopython
```

### Example: Create Sequence
```python
from Bio.Seq import Seq

dna = Seq("ATGCGT")
print(dna)
print("Complement:", dna.complement())
print("Reverse Complement:", dna.reverse_complement())
```

### Example: Transcription (DNA → RNA)
```python
dna = Seq("ATGCGT")
rna = dna.transcribe()
print(rna)
```

### Example: Translation (Protein)
```python
protein = dna.translate()
print(protein)
```

---

## 🟢 WEEK 3: Sequence Analysis using Biopython

### Topics:
- GC content
- Sequence slicing
- Motif finding

### Example: GC Content
```python
from Bio.SeqUtils import gc_fraction

dna = Seq("ATGCGCTA")
print("GC %:", gc_fraction(dna) * 100)
```

### Example: Motif Search
```python
dna = "ATGCGTATGAC"
motif = "ATG"

positions = []
for i in range(len(dna)):
    if dna[i:i+len(motif)] == motif:
        positions.append(i)

print("Motif positions:", positions)
```

### Mini Project:
- Find all start codons (ATG) in DNA

---

## 🟢 WEEK 4: Working with FASTA Files

### Topics:
- Reading biological datasets
- FASTA format
- Sequence parsing

### Example: Read FASTA File
```python
from Bio import SeqIO

for record in SeqIO.parse("sequence.fasta", "fasta"):
    print("ID:", record.id)
    print("Sequence:", record.seq)
    print("Length:", len(record.seq))
```

### Example: GC Content for Multiple Sequences
```python
from Bio.SeqUtils import gc_fraction

for record in SeqIO.parse("sequence.fasta", "fasta"):
    gc = gc_fraction(record.seq) * 100
    print(record.id, "GC%:", gc)
```

### Mini Project:
- Load FASTA file
- Print:
  - Sequence name
  - Length
  - GC %

---

## 🟢 WEEK 5: Sequence Alignment & BLAST (Basic)

### Topics:
- Sequence alignment
- Comparing DNA sequences
- Intro to BLAST

### Example: Pairwise Alignment
```python
from Bio import pairwise2

seq1 = "ATGCT"
seq2 = "ATGTT"

alignments = pairwise2.align.globalxx(seq1, seq2)

for align in alignments:
    print(align)
```

### Mini Task:
- Compare two DNA sequences
- Check similarity

---

## 🟢 WEEK 6: Machine Learning + Biology

### Topics:
- Disease prediction basics
- Classification models

### Example: Logistic Regression
```python
from sklearn.linear_model import LogisticRegression

X = [[80], [120], [150], [200]]
y = [0, 0, 1, 1]

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[130]]))
```

---

## 🟢 FINAL PROJECT

### Project Idea:
Bioinformatics + AI Tool

### Features:
- Input DNA sequence
- Analyze:
  - GC content
  - Motifs
- Load FASTA file
- Predict disease risk (simple model)

### Example:
```python
from Bio.Seq import Seq

dna = Seq("ATGCGCTA")
print("Protein:", dna.translate())
```

---

## 🎓 Skills You Gain

- Biopython library usage
- DNA/RNA/Protein analysis
- FASTA file handling
- Sequence alignment
- Basic machine learning

---

## 🚀 Outcome

You will be able to:
- Analyze real biological data
- Use Biopython tools
- Understand AI in healthcare
- Build beginner bioinformatics projects
