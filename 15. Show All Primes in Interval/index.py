# print all primes in interval

start = int(input("Enter the first number of the interval:"))
end = int(input("Enter the last number of the interval:"))

primeList = []

interval = range(start, end+1)

for num in interval:
    isPrime = True

    for i in range(2, num//2 + 1):
        if num % i == 0 and num != i:
            isPrime = False
    
    if isPrime:
        primeList.append(num)

print("The primes in this interval are: ")
print(primeList)