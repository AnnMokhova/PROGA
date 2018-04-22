#вариант 2: сколько найдено файлов, не содержащих цифр в названии

import os

def main():
   file_list = os.listdir()
   without_numb = []
   with_numb = []
   summa = 0
   for filename in file_list:
      if os.path.isfile(filename):
         if any(map(str.isdigit, filename)):
            with_numb.append(filename)
         if not filename in with_numb:
            summa += 1
            if not filename in without_numb:
               without_numb.append(filename)
   print('Всего найдено файлов, не содержащих цифр в названии: ', summa)
   print('Список этих файлов без повторов: ', ', '.join(without_numb))

main()
