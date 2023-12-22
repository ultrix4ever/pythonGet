s = input().lower()


for ch in [".", ",", "!", "?", ":", ";", "-"]:
    s = s.replace(ch, "")
    
slist = s.split()
result = {}
min_list = []

for words in slist:
    result[words] = result.get(words, 0) + 1

for key,val in result.items():
    if val == min(result.values()):
        min_list.append(key)

#print(result)

min_list = sorted(min_list)
print(min_list[0])