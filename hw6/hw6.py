import random
  # вариант 2: стихотворения с метрической схемой - хорей (четырехстопный)

def nouns_pl():
    with open ('nouns_pl.txt') as f:
        text = f.read()
        splited_text = text.split()
        nouns_pl = []
        for word in splited_text:
            nouns_pl.append(word)
    return random.choice(nouns_pl)

def nouns_m():
    with open ('nouns_m.txt') as f:
        text = f.read()
        splited_text = text.split()
        nouns_m = []
        for word in splited_text:
            nouns_m.append(word)
    return random.choice(nouns_m)

def nouns_n():
    with open ('nouns_n.txt') as f:
        text = f.read()
        splited_text = text.split()
        nouns_n = []
        for word in splited_text:
            nouns_n.append(word)
    return random.choice(nouns_n)

def nouns_f():
    with open ('nouns_f.txt') as f:
        text = f.read()
        splited_text = text.split()
        nouns_f = []
        for word in splited_text:
            nouns_f.append(word)
    return random.choice(nouns_f)


def adj_m():
    with open ('adj_m.txt') as f:
        text = f.read()
        splited_text = text.split()
        adj_m = []
        for word in splited_text:
            adj_m.append(word)
    return random.choice(adj_m)

def adj_n():
    with open ('adj_n.txt') as f:
        text = f.read()
        splited_text = text.split()
        adj_n = []
        for word in splited_text:
            adj_n.append(word)
    return random.choice(adj_n)

def adj_f():
    with open ('adj_f.txt') as f:
        text = f.read()
        splited_text = text.split()
        adj_f = []
        for word in splited_text:
            adj_f.append(word)
    return random.choice(adj_f)

def nouns_gen():
    with open ('nouns_gen.txt') as f:
        text = f.read()
        splited_text = text.split()
        nouns_gen = []
        for word in splited_text:
            nouns_gen.append(word)
    return random.choice(nouns_gen)

def trans_verbs():
    with open ('trans_verbs.txt') as f:
        text = f.read()
        splited_text = text.split()
        trans_verbs = []
        for word in splited_text:
            trans_verbs.append(word)
    return random.choice(trans_verbs)

def intran_verbs():
    with open ('intran_verbs.txt') as f:
        text = f.read()
        splited_text = text.split()
        intran_verbs = []
        for word in splited_text:
            intran_verbs.append(word)
    return random.choice(intran_verbs)

def adverbs():
    with open ('adverbs.txt') as f:
        text = f.read()
        splited_text = text.split()
        adverbs = []
        for word in splited_text:
            adverbs.append(word)
    return random.choice(adverbs)

def conj():
    with open ('conj.txt') as f:
        text = f.read()
        splited_text = text.split()
        conj = []
        for word in splited_text:
            conj.append(word)
    return random.choice(conj)

def punct():
    with open ('punct.txt') as f:
        text = f.read()
        splited_text = text.split(' ')
        punct = []
        for word in splited_text:
            punct.append(word)
    return random.choice(punct)


def verse1():
    return adj_m() + ' ' + nouns_m() + ' ' + trans_verbs() + ' ' + nouns_gen() + punct()

def verse2():
    return adj_f() + ' ' + nouns_f() + ' ' + intran_verbs() + ' ' + adverbs() + punct()

def verse3():
    return nouns_n() + ' ' + trans_verbs() + ' ' + nouns_gen() + ' ' + adverbs() + punct()

def verse4():
    return adj_n() + ' ' + nouns_n()+ ' '  + intran_verbs() + ' ' + adverbs() + punct()

def verse5():
    return nouns_m() + ' ' + intran_verbs() + ' ' + conj() + ' ' + nouns_m() + punct()

def verse6():
    return adj_f() + ' ' + nouns_f() + ' ' + trans_verbs() + ' ' + nouns_gen() + punct()

def verse7():
    return conj() + ' ' + nouns_pl() + ' ' + intran_verbs() + ' ' + nouns_f() + punct()

def make_verse():
    verse = random.choice([1,2,3,4,5,6,7])
    if verse == 1:
        return verse1()
    elif verse == 2:
        return verse2()
    elif verse == 3:
        return verse3()
    elif verse == 4:
        return verse4()
    elif verse == 5:
        return verse5()
    elif verse == 6:
        return verse6()
    else:
        return verse7()

for n in range(4):
    print(make_verse())
