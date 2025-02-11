import random

def generate_anagram(word):
    # Преобразуем слово в список символов для удобной работы с ними
    characters = list(word)
    
    # Перемешиваем символы слова случайным образом
    random.shuffle(characters)
    
    # Объединяем перемешанные символы обратно в строку
    anagram = ''.join(characters)
    
    return anagram

def main():
    word = input("Введите слово: ")
    
    if not word.isalpha():
        print("Пожалуйста, введите корректное слово, содержащее только буквы.")
    else:
        anagram = generate_anagram(word.lower())  # Приводим к нижнему регистру для простоты
        print(f"Случайная анаграмма слова '{word}': {anagram}")

if __name__ == "__main__":
    main()