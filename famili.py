count = int(input("Please enter the number of family members: "))
groups = {}
for i in range(count):
    name = input('Please enter the name: ')
    age = int(input('Please enter the age: '))
    if age in range(9):
        if groups.get('Child') is not None:
            groups['Child'] += [name]
        else:
            groups['Child'] = [name]
    elif age in range(9, 18):
        if groups.get('Teenager') is not None:
            groups['Teenager'] += [name]
        else:
            groups['Teenager'] = [name]
    elif age in range(18, 31):
        if groups.get('Young') is not None:
            groups['Young'] += [name]
        else:
            groups['Young'] = [name]
    elif age in range(30, 61):
        if groups.get('Adult') is not None:
            groups['Adult'] += [name]
        else:
            groups['Adult'] = [name]
print(groups)
