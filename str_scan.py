#my_str = input('Please enter your text:' )
#simbol_str = ('~!@#$%^&*()_+=-\/|')
#
#for simbol in my_str:
#	for x in simbol_str :
#		if simbol == x:
#			break
#		else:
#			continue
#print(simbol)


animals_1 = {"dog", "cat", "pig", "horse", "lamb"}
animals_2 = {"pig", "sheep", "rabbit", "dog"}
animals_3 = set()
for x in animals_1:
	for y in animals_2:
		if x == y:
			continue
		else:
			animals_3.add(x)
			animals_3.add(y)
print(animals_3)
