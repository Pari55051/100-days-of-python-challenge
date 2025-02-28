# check for prime number

num = int(input("Enter a number: "))
isPrime = True

for i in range(2, num//2 + 1):
    if num % i == 0 and num != i:
        isPrime = False


if isPrime:
    print("Is a Prime Number")
else:
    print("Not a Prime Number")
        