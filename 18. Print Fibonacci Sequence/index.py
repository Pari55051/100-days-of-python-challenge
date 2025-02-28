# print fibonacci sequence

num_terms = int(input("Enter the number of terms to display: "))

fibonacci_seq = []

for i in range(0, num_terms):
    term = 0

    if i == 0:
        fibonacci_seq.append(0)
    elif i == 1:
        fibonacci_seq.append(1)
    else:
        term = fibonacci_seq[i-1] + fibonacci_seq[i-2]
        fibonacci_seq.append(term)

print(fibonacci_seq)