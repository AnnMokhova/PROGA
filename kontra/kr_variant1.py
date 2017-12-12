with open ('Extinct_languages.tsv', 'r', encoding='utf-8') as f:
    #задание 1
    for line in f:
        if len(line) > 35:
            print(line)
    #задание2
    summ = 0
    for line in f:
        name, num, stat = line.split('\t')
        if stat == 'Critically endangered':
            summ += summ
    print('число языков со статусом ', summ)
    #задание3
    lang = input('введите название языка ')
    l_list = []
    l_list.append(lang)
    while lang != '':
        lang = input('введите название языка ')
        l_list.append(lang)
    name = line.split('\t')
    for name in line:
        for lang in l_list:
            if name == lang:
                print(line)
            else:
                print('название не встретилось в списке')
