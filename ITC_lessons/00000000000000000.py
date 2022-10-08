count = int(input("Please enter the count of family members: "))
age_groups = {}
for i in range(count):
    name = input('Please enter the name: ') 
    age = int(input('Please enter the age: '))
    if age in range(9): # կստուգի տարքիքը պատկանում է նշված միջակայքին, եթե ոչ ակնցնի հաջորդ պայմաններին
        if age_groups.get('Child') is not None: # Ստուգում է կա key-ը թե ոչ
            age_groups['Child'] += [name]  # Եթե կա ապա այդ key ին տալիս է name ի արժեքը լիստում
        else:
            age_groups['Child'] = [name] # Եթե key -ը չկա ապա կավեացնի և կտա name արժեքը լիստում
    elif age in range(9, 18):
        if age_groups.get('Teenager') is not None:
            age_groups['Teenager'] += [name]
        else:
            age_groups['Teenager'] = [name]
    elif age in range(18, 31):
        if age_groups.get('Young') is not None:
            age_groups['Young'] += [name]
        else:
            age_groups['Young'] = [name]
    elif age in range(30, 61):
        if groups.get('Adult') is not None:
            age_groups['Adult'] += [name]
        else:
            age_groups['Adult'] = [name]
print(age_groups)
