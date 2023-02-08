# Спрашиваем текст и определяем словари для больших и малых букв
text = input('Какой текст нужно зашифровать? \n').split()
upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Объявляем функцию
def caesar(text):

    # Находим длины слов в тексте и создаём из них список
    list_gisit = []
    for i in range(len(text)):
        count = 0
        for j in range(len(text[i])):
            if text[i][j].isalpha():
                count +=1
        list_gisit.append(count)    

    # Определяем номер индекса буквы в алфавите
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j].isalpha():
                
                if text[i][j].islower():
                    place = lower_alphabet.index(text[i][j])
                if text[i][j].isupper():
                    place = upper_alphabet.index(text[i][j])
                
                # Определяем номер нового индекса буквы в алфавите
                index = (place + int(list_gisit[i])) % len(upper_alphabet)

                # Выводим измененный символ.
                if text[i][j] == text[i][j].lower():
                    print(lower_alphabet[index], end='')
                if text[i][j] == text[i][j].upper():
                    print(upper_alphabet[index], end='')

            # Если text[i] не является буквой:
            else:
                # Делаем print этого символа без изменений.
                print(text[i][j], end='')
        # Добавляем пробел после каждого слова        
        print(' ', end='')     

# Объявляем функцию.
caesar(text)