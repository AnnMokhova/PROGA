import re

def open_file():
    with open('karenina.xml', encoding='utf-8') as f:
        text = f.read()
    return text

def tags(text):
    razbor = re.findall(r'<ana lex="(.*?)"', text)
    word = re.findall(r'<w>', text)
    sum_r = len(str(razbor))
    sum_w = len(str(word))
    print(sum_r // sum_w)

def dictionary(text):
    morph = re.findall(r'gr="([A-Z]*)', text)
    #print(morph)
    d = {}
    for key in morph:
        if key in d:
            value = d[key]
            d[key] = value + 1
        else:
            d[key] = 1
    with open('new.txt', 'w', encoding='utf-8') as fl:
        for key in sorted(d.keys()):
            written = "%s\t%s" % (key, d[key])
            fl.write(written + '\n')

tags(open_file())    #задание на 5 баллов
dictionary(open_file()) #задание на 8 баллов
