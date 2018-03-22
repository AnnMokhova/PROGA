#вариант 2: все формы глагола 'найти'

import re

def open_file(file):
    with open(file, encoding='utf-8') as f:
        f = f.read()
    f = f.lower()
    f = f.replace('\n', '')
    return f

def search():
    ask = input('введите название файла: ') #text.txt #najti.txt 
    text = open_file(ask)
    forms = re.findall(r'на[шй][ёлдт][ёлаоуия][ёшь]*с*ь*', text)
    for match in forms:
        print(match)

search()
