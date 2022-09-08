print("Enter the number of friends joining (including you):")
number_of_friends = int(input())
names = {}

if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(0, number_of_friends):
        firstname = input()
        names[firstname] = 0
    print("Enter the total bill value:")
    bill = input()
    bill_one_person = round(float(bill) / number_of_friends, 2)
    for i,j in names.items():
        names[i] = bill_one_person
    print(names)
# 2/4 8.09.2022 new
