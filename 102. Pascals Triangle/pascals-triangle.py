#print("Hello, World")
## Print pascal's triangle

#         0C0
#      1C0   1C1  
#  2C0    2C1    2C2
#3CO    3C1    3C2    3C3


from math import factorial

num_rows = 5

for i in range(num_rows):
    #left spacing
    for j in range(num_rows-i-1):
        print(end=" ")
    
    #combination --> nCr = n! / [(n-r)! * r!]
    for j in range(i+1):
        nCr = factorial(i) // (factorial(i-j) * factorial(j))

        print(nCr, end=" ")
    
    print()