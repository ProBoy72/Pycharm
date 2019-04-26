from random import randint

x = randint(0, 10)
i = 0
while i < 1:
    guess = input('guess the number ')
    if (guess < str(x)):
        print('number is bigger than ' + guess)
    elif (guess > str(x)):
        print('guess is smaller than ' + guess)
    else:
        i = 1

print('correct ')