# Python Program to Check if a Number is Positive, Negative or 0

num = int(input("Enter a number: "))

if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
elif num == 0:
    print(num, "is zero")
else:
    print("Error!!")