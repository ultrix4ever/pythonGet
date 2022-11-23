n = input()
n = int(n[1:])
endList = []
for i in range(n):
    s = input()
    if '#' in s:
        sInd = s.find('#')
        s = s[0:sInd]
        s = s.rstrip()
    endList.append(s)
print(*endList, sep='\n') 

    