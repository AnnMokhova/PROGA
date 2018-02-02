a_list = []
s = 0
a = input('Введите число ')
while a != '':
    a_list.append(int(a))
    a = input('Введите число ')
for i in a_list:
    s += i
n = len(a_list)
if n != 0:
    sr_ar = s / n
    print ('Среднее арифметическое = ', sr_ar)
    print('Максимальное число = ', max(a_list))
    print('Минимальное число = ', min(a_list))
else:
    print('Нет введенных чисел')
