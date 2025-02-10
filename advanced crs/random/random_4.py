import random

lot = []

for i in range(7):
    lot.append(random.randint(1, 49))


print(*sorted(lot))