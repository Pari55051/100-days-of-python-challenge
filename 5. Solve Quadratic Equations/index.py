# Python Program to Find Roots of a Quadratic Equation

# imports
import math

# get coefficient values
a = int(input("Enter the value of coefficient of x^2: "))
b = int(input("Enter the value of coefficient of x: "))
c = int(input("Enter the value of constant: "))

# find roots function
def findRoots(a, b, c):
    
    # find discriminant value
    discriminant = (b**2) - (4*a*c)
    sqrt_dis = math.sqrt(abs(discriminant))

    if discriminant > 0:
        # [real + distinct roots]
        print("The roots are: ", ((-b + sqrt_dis) / 2*a), "and", ((-b - sqrt_dis) / 2*a))

    elif discriminant == 0:
        # [equal roots]
        print("The roots are", ((-b + sqrt_dis) / 2*a))

    elif discriminant < 0:
        print("Complex Roots")

    else:
        print("Error!!")
    

if a == 0:
    print("Error : Incorrect Quadratic Equation. Coefficient of 'x^2' should not be zero")
else:
    findRoots(a, b, c)
