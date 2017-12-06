word = input('Введите слово для 2 варианта: ')
w_list = []
w_list.append(word)
while word != '':
  word = input('Введите слово: ')
  w_list.append(word)
f = open('text.txt', 'w')
for word in w_list:
  if len(word) > 5:
    f.write(word + '\n')
f.close()
