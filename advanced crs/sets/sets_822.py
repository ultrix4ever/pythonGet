n = int(input())
m = int(input())
k = int(input())
x = int(input())
y = int(input())
z = int(input())
t = int(input())
a = int(input())

only_one = n + m + k - (x + y + z - t)
two_books = x + y + z - 2*t
no_books = a - only_one - two_books - t

print(only_one)
print(two_books)
print(no_books)