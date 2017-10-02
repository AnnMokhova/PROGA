word = str(input('введите слово для задания 2 варианта: '))
for i in range(len(word)):
    if (i % 2 == 0) and (word[i] == 'п' or word[i] == 'о' or word[i] == 'е'):
        print(word[i])
