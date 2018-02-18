import random

def words_dict():
    with open('words.csv', encoding='utf-8') as f:
        d = {}
        for line in f:
            line = line.replace('\n','')
            word, hint = line.split(',')
            if word in d:
                d[word].append(hint)
            else:
                d[word] = [hint]
    return d

def ask_word():
    word = random.choice(list(words_dict().keys()))
    hint = random.choice(words_dict()[word])
    podskaska = ''
    len_word = len(word)
    while len_word > 0:
        podskaska += '.'
        len_word = len_word - 1
    print('Количество точек после подсказки совпадает с количеством букв в слове')
    print(hint, podskaska)
    x = input('Введите слово: ')
    if x == word:
        print('Вы угадали)))')
    else:
        print('Вы не угадали(((')
        print('Попробуйте еще раз')
        y = input ('Введите слово: ')
        while y!= word:
            new_hint = random.choice(words_dict()[word])
            print(new_hint, podskaska)
            y = input ('Введите слово: ')
        print('Ура! Вы наконец-то угадали)))')

ask_word()
