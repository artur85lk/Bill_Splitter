import random

print("Enter the number of friends joining (including you):")
number_of_friends = int(input())
print()
names = {}
def lucky_man(choice, bill):
    if choice == "Yes":
        lucky_name = random.choice(list(names.keys()))
        print(f"{lucky_name} is the lucky one!")
        newbill = round(float(bill) / (number_of_friends - 1), 2)
        for i,j in names.items():
            if i == lucky_name:
                names[lucky_name] = 0
            else:
                names[i] = newbill
    else:
        print("No one is going to be lucky")

if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(0, number_of_friends):
        firstname = input()
        surname = "0"
        names[firstname] = 0
    print()
    print("Enter the total bill value:")
    bill = input()
    print()
    bill_one_person = round(float(bill) / number_of_friends, 2)
    for i,j in names.items():
        names[i] = bill_one_person
    # print(names)
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input()
    print()
    lucky_man(choice,bill)
    print()
if number_of_friends > 0:
    print(names)
