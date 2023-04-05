
def  chunked(list, num):
    
    for i in range(0, len(list), num):
        list_main.append(list[i:i+num])
    
    return list_main
        
    


list = input().split()
num = int(input())
list_main = []

print(chunked(list, num))