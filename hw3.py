word = list(input('введите слово для 2 варианта '))
for i in range(len(word)+1):
    word=''.join(word)
    if i != 0:
        print(word[:i])
