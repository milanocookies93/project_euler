def largestprimefactor(x):
	y = 2
	while y != x:
		if x%y == 0:
			x = x/y
			y = 2
		else:
			y = y + 1
	return x

print largestprimefactor(600851475143)
