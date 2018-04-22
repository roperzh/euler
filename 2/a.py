def fibonacci():
	x, y = 0, 1
	while x < 4*10**6:
		yield x
		x, y = y, x + y

def evenNum():
	return sum(i for i in fibonacci() if i % 2 == 0)

print(evenNum())