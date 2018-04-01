#вариант 2

import re

def open_file(file):
    with open(file, 'rb') as f:
        f = f.read()
    return f

def search_write():
    ask = input('Введите название города, часовой пояс которого вы хотите узнать ') #Москва Берлин Нью-Йорк
    if ask == 'Москва':
        doc = 'Moscow.html'
    if ask == 'Берлин':
        doc = 'Berlin.html'
    if ask == 'Нью-Йорк':
        doc = 'NY.html'
    text = open_file(doc)
    result = re.search(r'Часовой пояс (\S+\s+\S+)', text.decode('utf-8'), re.I | re.U)
    with open('text.txt', 'w') as empty_file:
        empty_file.write(result.group())
    print('Откройте файл text.txt, чтобы узнать часовой пояс указанного города')

search_write()
