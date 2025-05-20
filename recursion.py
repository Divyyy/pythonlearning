# Recursion = a function that calls itself to do a smaller job.

# It keeps going until it hits a stopping point (base case).

# Then everything is put back together like a puzzle

# example of recursion

def fib(n):
    if(n == 0 or n == 1):
        return n
    return fib(n-2) + fib(n-1)
print(fib(6))