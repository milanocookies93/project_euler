curr = 1
prev = 1
tot = 0
while 4000000>curr:
        curr += prev
        prev = curr - prev
	if prev%2 == 0:
		tot += prev
print tot
