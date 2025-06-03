import random

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_strings(length=1):
    letters = '@#$%&*()_+[]{}|<>?'
    return ''.join(random.choice(letters) for i in range(length))

pass1 = generate_random_string(6)
pass2 = generate_random_strings(1)
pass3 = generate_random_string(5)

password = pass1
print("suggested password:", password)
