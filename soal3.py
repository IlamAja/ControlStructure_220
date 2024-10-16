def fibonacci_series(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    result = []
    
    while a <= n:
        result.append(a)
        a, b = b, a + b  # Update to next Fibonacci numbers
    
    return result

# Input the value of n
n = int(input("Enter the value of n: "))

# Generate and print the Fibonacci series
fibonacci = fibonacci_series(n)
print(f"Fibonacci series up to {n}: {fibonacci}")
