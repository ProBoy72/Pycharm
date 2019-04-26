def encrypt(name):
    enc = ''
    i = len(name) - 1
    while i >= 0:
        enc += name[i]
        i -=1
    print(enc.replace(' ', '_'))
enter = input('Enter your name ')
encrypt(enter)
