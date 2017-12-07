#def say_hello():
#    print('hello')

#say_hello()

#def say_hello(m, n):
#    print(m)
#    print(n)

#say_hello(5, 6)

#n = 7
#m = 8

#def say_hello(n, m):
#    n = 9
#    m = 10
#    print(n)
#    print(m)

#say_hello(5, 6)

#print(n)
#print(m)

#n = 7
#m = 8

#def say_hello(n, m):
#    x = n + m
#    return x

#y = say_hello(5, 6)

#print(y)

def say_hello(n, m):
    return n + m

def say_hello2(n, m):
    return n - m

def main():
    n = input('введите первую переменную: ')
    m = input('введите вторую переменную: ')
    x = say_hello(n, m)
    y = say_hello(x, m)
    print(y)
main()
