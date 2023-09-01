
words = input().lower().split()
set_words = set()
for i in range(len(words)):
     set_words.add(words[i].strip('.,;:-?!'))
print(len(set_words))

      
      ###

words = input().lower().split()
set_words = {word.strip('.,;:-?!') for word in words}
print(len(set_words))