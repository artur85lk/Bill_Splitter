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
    print(names)