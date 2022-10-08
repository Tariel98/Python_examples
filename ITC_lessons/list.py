nums = [1, -8, 2, 10, 6, -3, 4, -12, -15, 5, 6]
neg_nums = list()
for x in nums:
	if x < 0:
		neg_nums.append(x)
print(f'Negativ numbers are: {neg_nums}')
	
print(f'The arithmeric average = {sum(neg_nums) / len(neg_nums)}')	

