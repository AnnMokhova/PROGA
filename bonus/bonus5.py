cons = 'qwrtpsdfghjklzxcvbnm'
word = input('Введите слово на английском ')
for i in word:
    if i in cons:
        i = i + 'aig'
        print (i, end = '')
    else:
        print (i, end = '')
