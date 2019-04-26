from random import randint

name = input('Enter your name: ')
x = randint(0,1)
if(x == 1):
    print(name +  ' is gay')
else:
    print(name + ' is not gay')