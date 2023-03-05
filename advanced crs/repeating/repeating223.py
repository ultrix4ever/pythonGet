
string = input()    
numbers = list(map(int, string.split()))  

for i in range(0, len(numbers)-1, 2):
    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]


print(' '.join(map(str, numbers)))