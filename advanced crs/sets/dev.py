n = int(input()) # количество учеников, поехавших на море
m = int(input()) # количество учеников, съездивших в деревню
k = int(input()) # количество учеников, сходивших в горы
x = int(input()) # количество учеников, побывавших и на море, и в деревне
y = int(input()) # количество учеников, побывавших и в деревне, и в горах
z = int(input()) # количество учеников, которые никуда не ездили и писали ДВИ по математике

total = n + m + k - x - y + z
print(total)