print('Prime numbers between 900 and 1000 are:')

for x in range(21):
	if x >1:
		for num in (2,x):
			if x % num == 0:
				break
			else:
				print(x)
