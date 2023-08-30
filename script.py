def generate_fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence

# Get input from the user
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

# Generate the Fibonacci sequence
fibonacci_sequence = generate_fibonacci(num_terms)

# Display the sequence
print("Fibonacci Sequence:")
for term in fibonacci_sequence:
    print(term, end=" ")
