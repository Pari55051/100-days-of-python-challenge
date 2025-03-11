# find nums divisible by other num


num_list = input("Enter the list as space-separated values: ").split()
#print(num_list)
divisor = int(input("Enter the divisor: "))

div_list = []

for num in num_list:
    if float(num) % divisor == 0:
        div_list.append(num)


print("Numbers divisible by", divisor, "are:", div_list)