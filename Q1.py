# Fibonacci Using Memoization

# Accept an integer N
N = int(input("Enter the number of terms: "))

# Dictionary to store previously calculated values
memo = {}

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Check if value is already calculated
    if n in memo:
        return memo[n]

    # Calculate and store the value
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]


# Generate and display first N Fibonacci numbers
print("Fibonacci sequence:")

for i in range(N):
    print(fibonacci(i), end=" ")


'''
Enter the number of terms: 8
Fibonacci sequence:
0 1 1 2 3 5 8 13 
'''