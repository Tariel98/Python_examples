def printer():
	print('This is in file1.py')

def generate_odd_nums():
	for i in range(50):
		if i % 2 != 0:
			yield i

def print_hello():
	print("Hello")

odd_nums = generate_odd_nums()

for x in odd_nums:
	print(x)
