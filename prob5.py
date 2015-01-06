def smallestdiv(x):
	if x==2:
		return 2
	multiplier = x
	div = 1
	while (div < x):
		if multiplier%div == 0:
			multiplier = multiplier/div
		div = div + 1
	return multiplier*smallestdiv(x-1)

print smallestdiv(10)
