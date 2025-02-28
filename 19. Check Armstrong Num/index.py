# check if given number is armstrong number

num = str(int(input("Enter a number: ")))

val = 0

for n in num:
    val += int(n)**len(num)

if int(num) == val:
    print("Is an Armstrong Number")
else:
    print("Not an Armstrong Number")
