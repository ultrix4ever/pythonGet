s = input().split()
s_new = []
counter = {}
for word in s:
    if word not in counter:
        counter[word] = 0
        s_new.append(word)
    else:
        counter[word] += 1
        s_new.append(f"{word}_{counter[word]}")
print(' '.join(s_new))