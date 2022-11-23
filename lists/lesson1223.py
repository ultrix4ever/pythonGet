TelNumber = input()

if len(TelNumber) == 12:
    if TelNumber[0:3].isdigit() == True and TelNumber[4:7].isdigit() == True and TelNumber[9::].isdigit() == True:
        print('YES')
    else:
        print('NO')
if len(TelNumber) == 14:
    if TelNumber[0] == '7' and TelNumber[2:5].isdigit() == True and TelNumber[6:9].isdigit() == True and TelNumber[10::].isdigit() == True:
        print('YES')
    else:
        print('NO')

if len(TelNumber) != 12 and len(TelNumber) != 14:
    print('NO')

