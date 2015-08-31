def collatz(num, count=0):
	count += 1
	if num == 1:
		return count
	if num % 2 == 1:
		return collatz(num*3 + 1, count)
	return collatz(num/2, count)
