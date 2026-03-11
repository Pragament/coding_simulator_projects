# Arithmetic Progression Generator (Console Version)

a = 1   # First term
d = 4   # Common difference
n = 1   # Term number

def calculate_sum_formula(n, a, d):
    t1 = n / 2
    t2 = 2 * a
    t3 = d * (n - 1)
    return t1 * (t2 + t3)

print("Arithmetic Progression Generator")
print("First term (a):", a)
print("Common difference (d):", d)

while True:
    print("\nCurrent term number (n):", n)
    print("Nth Term:", a + (n - 1) * d)
    print("Formula Result:", calculate_sum_formula(n, a, d))

    choice = input("\nPress 'b' for next term, 'a' for previous term, 'q' to quit: ")

    if choice.lower() == 'b':
        n += 1
    elif choice.lower() == 'a':
        if n > 1:
            n -= 1
        else:
            print("Already at first term!")
    elif choice.lower() == 'q':
        break
    else:
        print("Invalid input!")