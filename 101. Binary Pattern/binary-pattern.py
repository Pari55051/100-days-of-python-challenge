print("hello world")

for i in range(0, 5+1):
    for j in range(1, i+1):
        #print(j, end="")
        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    
    print()
