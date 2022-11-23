text = input()
text1 =''
for i in range(0, len(text)):
    if text[i].isupper() == True:
        text1 += '_'
    text1 += text[i].lower()
text = text1[1:]


print(text)