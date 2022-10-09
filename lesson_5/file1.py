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


class Number:
	
	def __init__(self, number):
		self.number = number

	def odd_number(self):
		my_odd_list  = []
		for x in range(self.number):
			if x % 2 == 0:
				my_odd_list.append(x)
#			else:
#				continue
		return my_odd_list

	def env_number(self):
		my_env_list = []
		for x in range(self.number):
			if x % 2 != 0:
				my_env_list.append(x)
#			else:
#				continue
		return my_env_list

	def __del__(self):

odd = Number(50)
print(odd.odd_number())
print(odd.env_number())
