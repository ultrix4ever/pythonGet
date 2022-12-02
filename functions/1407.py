# объявление функции
def is_pangram(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(abc)):
        text = text.lower()
        if abc[i] in text:
            Flag = True
        else:
            Flag = False
            break
    return Flag



# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))