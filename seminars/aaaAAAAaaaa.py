import random

def get_words_dict():
    d = {}
    with open('words.csv', encoding='utf-8') as f:
      hint = ''
      for line in f:
        if line == 'slovo,podskaska\n':
            continue
        if hint == '':
            word, hint = line.split(',', maxsplit=1)
        else:
            hint += line
        if line == '"\n':
            words_dict = d.setdefault(word, {})
            hint_list = words_dict.setdefault(hint, [])
            hint_list.append(hint)
            hint = ''
    return d

def choose_word(d):
    chosen_word = random.choice(word_dict(d))
    for word, word_dict in d:
        for hint, hint_list in word_dict:
            print (hint)
    return choose_word

def podskaska(choose_word):
    hint_len = len(choose_word(d))
    podskaska = ''
    while hint_len > 0:
        podskaska += '.'
        hint_len = hint_len - 1
    return podskaska

choose_word(d)
print(podskaska(choose_word))
x = input('введите слово ')
if x == chosen_word(choose_word(d)):
    print('вы угадали)))')
else:
    print('вы не угадали')
