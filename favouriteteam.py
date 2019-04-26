from random import randint
friends = input('how many friends do you have ')
friends = int(friends)
teams = ['barcelona','real madrid','manchester city','manchester united','chelsea','arsenal','bayern munchen','juventus']
sent = ''
if (friends == 0):
    x = randint(0,7)
    name = input('enter your name: ')
    print(name + "'s favourite team is " + teams[x])
for i in range (0,friends):
    x = randint(0, 7)
    name = input('enter your name: ')
    sent += name + "'s favourite team is " + teams[x] + "\n"

print(sent)
