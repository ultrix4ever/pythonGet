num = int(input())
twns = set()
for i in range(num):
    twns.add(str(input()))
new_twn = str(input())
if new_twn not in twns:
    print('OK')
else:
    print('REPEAT')
    