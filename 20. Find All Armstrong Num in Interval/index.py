# find all armstrong numbers in interval

start = int(input("Enter the first number of the interval:"))
end = int(input("Enter the last number of the interval:"))

armstrongList = []

interval = range(start, end+1)

for num in interval:
    num = str(num)
    val = 0
    isArmstrong = False

    for n in num:
        val += int(n)**len(num)
    
    if int(num) == val:
        armstrongList.append(num)
    

print("The armstrong number in this interval are: ")
print(armstrongList)