# display the multiplication table of a number

num = int(input("Enter a number: "))

for i in range(1, 10+1):
    print(num, "X", i, "=", num*i)