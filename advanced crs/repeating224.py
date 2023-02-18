

string = input()    
numbers = list(map(int, string.split()))  
numbers2 = []
numbers2.append(numbers[-1]) 
for i in range(len(numbers)-1):
    numbers2.append(numbers[i]) 
print(*numbers2)
