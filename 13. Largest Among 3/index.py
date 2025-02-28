# Python Program to Find the Largest Among Three Numbers

a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))
c = eval(input("Enter third number: "))

largest = 0

if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
elif c > a and c > b:
    largest = c
else:
    largest = "Error! Don't Input Equal Numbers"

print("Largest number is: ", largest)