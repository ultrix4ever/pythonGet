import random

def generate_ip():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip
print(generate_ip())