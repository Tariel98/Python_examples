boys = int(input('Enter count of boys: '))
girls = int(input('enter count of girls: '))
answer = ''

if (boys > 2 * girls) or (girls > 2 * boys):
	print('Not resh')
elif boys >= girls:
	k = boys - girls
	for bgbg in range(k):
		answer += 'BGB'
	for bg in range(girls - k):
		answer += 'BG'
else: 
	k = girls - boys
	for gbgb in range(k):
		answer += 'GBG'
	for gb in range(boys - k):
		answer += 'GB'		

print(answer)
