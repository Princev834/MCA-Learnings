n = int(input("Enter how many terms: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print("Fibonacci series:", a)
else:
    print("Fibonacci series:", a, b, end=" ")
    for _ in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c