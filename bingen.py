from random import randint

bin = input('Enter Bin: ')
for i in range(0,10):
    x = randint(0,9)
    bin = bin.replace('x', str(x),1)

print(bin)