num = int(input("Enter a number:"))

def factorial(n):
    if n<2 and n!=0:
        return 1
    elif n == 0: return 0
    else:
        n = n * factorial(n-1)
        return n


res = factorial(num)

print(f"Factorial of {num} is: {res}")