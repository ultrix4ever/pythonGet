# объявление функции
def draw_box():
    print('*'*10)
    for i in range(12):
        print('*', ' '*8, '*', sep='')
    print('*'*10)

# основная программа
draw_box()  # вызов функции