# find factorial of given number manually

num = int(input("Enter a number: "))

def findFactorial (num):
    factorial = 1

    for i in range(1, num+1):
        factorial *= i
    
    return factorial


if num == 0:
    print("Factorial is: 1")
else:
    print("Factorial is: ", findFactorial(num))