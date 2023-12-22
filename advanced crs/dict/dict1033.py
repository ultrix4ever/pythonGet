text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for letters in text:
    result[letters] = result.get(letters, 0) + 1

print(result)