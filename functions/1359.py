# объявление функции
def convert_to_python_case(text):
    text1 =''
    for i in range(0, len(text)):
        if text[i].isupper() == True:
            text1 += '_'
        text1 += text[i].lower()
    text = text1[1:]
    return text
    
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))