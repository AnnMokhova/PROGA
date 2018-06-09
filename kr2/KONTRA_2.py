import re
import collections
import operator

def open_file(): 
    with open('mystem.xml', encoding='utf-8') as f:
        text = f.read()
    return text

def count_symbols(text): 
    n = 0
    for line in text:
        if '<w>' or '<se>' or '/se' in line:
            for symbol in line:
                n += 1
    return n

def write(n): 
    with open('text_write.txt', 'w', encoding='utf-8') as fl:
        fl.write(str(n))        

def dictionary(text): 
    morph = re.findall(r'gr="(.*?)"', text)
    d = {}
    for key in morph:
        if key in d:
            value = d[key]
            d[key] = value + 1
        else:
            d[key] = 1
    return d

def final(d): 
    from operator import itemgetter
    f = sorted(d.items(), key=itemgetter(1), reverse=True)
    with open('text_write2.txt', 'w', encoding='utf-8') as fl:
        for el in f:
            fl.write(str(el) + '\n')

def verbs(text): 
    verbs = re.findall(r'gr="(.*?)сов(.*?)ед(.*?)"', text)
    with open('text_write3.txt', 'w', encoding='utf-8') as fl:
        fl.write(str(len(verbs)))
    return verbs

def main():
   open_f = open_file()
   count = count_symbols(open_f)
   diction = dictionary(open_f)
   write(count)
   d_final = final(diction)
   verbs(open_f)

main()
