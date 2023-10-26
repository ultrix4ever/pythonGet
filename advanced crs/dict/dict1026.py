
def text_to_presses(text):
    dict_tp = {'1':['.',',','?','!',':'], 
               '2':['A','B','C'], 
               '3':['D','E','F'], 
               '4':['G','H','I'],  
               '5':['J','K','L'],
               '6':['M','N','O'],
               '7':['P','Q','R','S'],
               '8':['T','U','V'],
               '9':['W','X','Y','Z'],
               '0':[' ']
               }
    text = text.upper()
    result = ""
    for char in text:
        for key, values in dict_tp.items():
            if char in values:
                result += key * (values.index(char) + 1)
    return result

print(text_to_presses(input()))
