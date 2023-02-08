# объявление функции
def find_all(target, symbol):
    List = []
    for i in range(len(target)):
        if target[i] == symbol:
            List.append(i)
    return List

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
