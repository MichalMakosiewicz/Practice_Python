import random
import string

def weak_password():
    password = []
    for i in range(6):
        password.append(random.choice(string.ascii_lowercase))
    password = ''.join(password)
    return password

def medium_password():
    password = []
    for i in range(8):
        password.append(random.choice(string.ascii_letters))
    password = ''.join(password)
    return password

def hard_password():
    password = []
    for i in range(7):
        password.append(random.choice(string.ascii_letters))
    for i in range(3):
        password.append(str(random.randint(0, 9)))

    password = ''.join(password)
    return password


a = input("JAkie hasło(weak/medium/hard): ")

if a == 'weak':
    print(weak_password())
elif a == 'medium':
    print(medium_password())
elif a == 'hard':
    print(hard_password())
