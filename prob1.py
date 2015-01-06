def sumdivby(x,num):
	a = 0
	while x%num !=0:
		x = x-1
	while x > 0:
		a += x
		x = x - num
	return a

question=999
print sumdivby(question,3) + sumdivby(question,5) - sumdivby(question,15)
