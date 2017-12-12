with open ('Extinct_languages.tsv', 'r', encoding='utf-8') as f:
    #задание 1
    for line in f:
        if len(line) > 35:
            print(line)
    #задание2
    summ = 0
    for line in f:
        name, num, definit = line.split('/t')
        if definit == 'Critically endangered':
            summ += summ
            print('число языков со статусом ', summ)
            
            
