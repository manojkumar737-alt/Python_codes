import random
import string

def generate_random_string(length=4):
    password = ""
    for i in range(length):
        password += random.choice(string.punctuation)
        password += random.choice(string.digits)
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
    print("suggested password:", password)


generate_random_string(4)
