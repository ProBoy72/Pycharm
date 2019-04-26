from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
name = input('Enter Your name ')
token = f.encrypt(b'name')
encryption = str(token)
encryption = encryption.replace("'", '')
print(encryption)