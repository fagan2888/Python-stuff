from sys import argv
def fib(order):
    if order <= 0:
        return 1
    else:
        return fib(order-1) + fib(order-2)
total = 0
i = 0
num = 0
while num <= 4000000:
    num = fib(i)
    if num % 2 == 0:
        total += num
    i += 1
print(total)
