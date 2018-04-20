multiples = 0
iteration = 0
while iteration != 1000:	
	if iteration % 3 == 0 or iteration % 5 == 0:
		multiples += iteration
	iteration += 1

print(multiples)
