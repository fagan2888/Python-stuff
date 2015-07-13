primes = []
composites = []
num = 2
while len(primes) != 10001:
    if num not in composites:
        primes.append(num)
        for mult in range(num, 1000):
            composites.append(num*mult)
    print(len(primes)/10001)
    num += 1
print(primes)
