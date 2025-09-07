import math

def lcm_gcd(a, b):
    gcd = math.gcd(a, b)           
    lcm = math.lcm(a, b)           
    return lcm, gcd

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lcm, gcd = lcm_gcd(num1, num2)
print(f"GCD of {num1} and {num2} is: {gcd}")
print(f"LCM of {num1} and {num2} is: {lcm}")