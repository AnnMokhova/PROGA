#вариант 2
import collections

def words():
    with open ('text1.txt', encoding='utf-8') as f:
        text = f.read()
    text = text.lower()
    splited_text = text.split()
    return words

def ness(words):
    ness = []
    for word in words:
        if word[:-4] == 'ness':
            ness.append(word)
    return ness

def dic(ness):
    dic = {}
    c = collections.Counter(dic)
    for word in dic:
        c[word] += 1
    print('всего слов, оканчивающихся на -ness: ', c)
    print('наиболее частотное из них: ', Counter(dic).most_common(1))
    return dic

def main():
    dic(ness)
    freq(ness)

main()
