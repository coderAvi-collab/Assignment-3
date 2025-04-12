import  math

num = int(input("Enter a number:"))

def math_function(n):
    print(f"Square root:", math.sqrt(n))
    print(f"Logarithm:", math.log(n))
    print(f"Sine:", math.sin(n))

math_function(num)