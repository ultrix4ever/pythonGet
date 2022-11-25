# объявление функции
def is_palindrome(text):
    text = text.translate({ord(i): None for i in ' ,.!?-'})
    text = text.lower()
    if text == text[::-1]:
        return True
    else:
        return False
# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))