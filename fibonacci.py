def fibonacci(n):
    fib_series = [0, 1]  # Pehle do numbers
    for i in range(2, n):
        next_number = fib_series[-1] + fib_series[-2]  # Pichle do numbers ka sum
        fib_series.append(next_number)  # List mein add karo
    return fib_series[:n]  # Sirf n numbers return karo

# User se input lena
num = int(input("Enter the number of Fibonacci terms: "))
print(fibonacci(num))  # Output print hoga
