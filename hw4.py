with open('text.txt') as f:
    longest = 0
    shortest = 10^20
    for line in f:
        length = len(line)
        if length > longest:
            longest = length
        elif length < shortest:
             shortest = length
        else:
            print('пустой файл')
result = longest//shortest
print('во сколько раз самая короткая короче самой длинной: ', result)

