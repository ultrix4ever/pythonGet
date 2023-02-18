def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1

n = int(input("Enter the number of people in the circle: "))
k = int(input("Enter the step size: "))

print(josephus(n, k))