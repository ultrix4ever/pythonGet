# объявление функции
def is_correct_bracket(text):
    counter = 0
    for i in range(len(text)):
        if text[i] == '(':
            counter +=1 
        if text[i] == ')':
            counter -=1
        if counter < 0 :
            break
    if counter == 0 and text[0] == '(' and text[-1] == ')' :
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))