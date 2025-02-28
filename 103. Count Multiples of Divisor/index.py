print("enter five numbers below:")
num1 = float(input("first number: "))
num2 = float(input("second number: "))
num3 = float(input("third number: "))
num4 = float(input("fourth number: "))
num5 = float(input("fifth number: "))

num_list = [num1, num2, num3, num4, num5]

divisor = float(input("enter the division number:"))
count = 0

print("multiples of", divisor, "are:")
for n in num_list:
    remainder = n % divisor
    if remainder == 0:
        print(n, sep="")
        count += 1

print()
print(count, "multiples of", divisor, "found")
