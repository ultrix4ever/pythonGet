numbers = [print(int(i)**2, end=' ') for i in input().split() if (int(i)**2)%2 == 0 and (int(i)**2)%10 != 4 ]
