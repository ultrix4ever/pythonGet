

string = input()    
numbers = list(map(int, string.split()))  
count = 1

for i in range(len(numbers)-1):
    if numbers[i] != numbers[i+1]:
        count +=1
print(count)