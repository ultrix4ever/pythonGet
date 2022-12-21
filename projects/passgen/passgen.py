import random

digits = list('0123456789')
lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
punctuation = list('!#$%&*+-=?@^_')
ext_simbols = ['i', 'l', '1', 'L', 'o', '0', 'O']
count_pass = int(input('Сколько паролей создавать? : '))
lenght = int(input('Какая длина каждого пароля? : '))
chars = []
is_digits_pass = input('Включать ли цыфры? д\н : ')
is_uppercase_letters = input('Включать ли прописные буквы? д\н : ')
is_lowercase_letters = input('Включать ли строчные буквы? д\н : ')
is_punctution = input('Включать ли символы? д\н : ')
is_ext_simbols = input('Исключать ли неоднозначные символы "il1Lo0O" д\н : ')
    
if is_digits_pass in ['да', 'lf', 'l', 'д', 'yes']:
                chars = digits
if is_uppercase_letters in ['да', 'lf', 'l', 'д', 'yes']:
                chars += uppercase_letters
if is_lowercase_letters in ['да', 'lf', 'l', 'д', 'yes']:
                chars += lowercase_letters
if is_punctution in ['да', 'lf', 'l', 'д', 'yes']:
                chars += punctuation
if is_ext_simbols in ['да', 'lf', 'l', 'д', 'yes']:
    for i in range(len(ext_simbols)): 
        if ext_simbols[i] in chars:
            chars.remove(ext_simbols[i])
          
def pass_gen():
    passwd = []
    for i in range(lenght):
        passwd += random.choice(chars) 
    return passwd

for i in range(count_pass):
    print(*pass_gen(), sep='')

    
