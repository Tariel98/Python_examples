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

# unfinished business

class Number:
	
	def __init__(self, number, mode="odd" ):
		self.number = number
		self.mode = mode

	def result_list(self):
		my_odd_list  = []
		my_env_list = []

		for x in range(self.number):
			if self.mode == "odd":
				if x % 2 == 0:
					my_odd_list.append(x)
			elif self.mode == "evn":
				my_env_list.append(x)

		return my_odd_list



odd = Number(50)
print(odd.odd_number())
print(odd.env_number())
