
m = float(input())
rst = float(input())

IMT = m/(rst*rst)

if IMT > 25:
    print('Избыточная масса')
elif IMT < 18.5:
    print('Недостаточная масса')
else:
    print('Оптимальная масса')

