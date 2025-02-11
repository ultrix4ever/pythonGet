import random
import string

print(string.ascii_uppercase)

def generate_index():
    a = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randint(0, 99)) + '_' + str(random.randint(0, 99)) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
    return a

print(generate_index())
    