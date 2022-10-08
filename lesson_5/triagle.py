def __main():
	__perimeter_of_midlines(a = 14, b = 7, c = 10)

def __triangle_midlines(a,b,c):
	a = a / 2
	b = b / 2
	c = c / 2
	print(f'Parallel to side a is the length of the midline: {a}')
	print(f'Parallel to side b is the length of the midline: {b}')
	print(f'Parallel to side c is the length of the midline: {c}')
	return a, b, c

def __perimeter_of_midlines(a,b,c):
	p = sum(__triangle_midlines(a,b,c))
	print(f'The perimeter of the midlines will be: {p}')


__main()
