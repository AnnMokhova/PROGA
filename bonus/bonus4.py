vow = 'ёуеыаоэяию'
word = input('Введите слово ')
for i in word:
    if i in vow:
        i = i + 'c' + i
        print(i, end = '')
    else:
        print (i, end = '')
