def num1():
    a=input("Введите имя:")
    b=input("Введите возраст")
    for i in range(10):
        print(f"Меня зовут{a},мне {b} лет")
def num2():
    cifra=int(input("Введите число от 1 до 9:"))
    if cifra>0:
        for i in range(10):
            print(cifra*i)
def num3():
    for xd in range(0,100,3):
        print(xd)
def num4():
    inp=int(input("Введите число:"))
    start=1
    for i in range(1,inp+1):
        start=start*i
    print(start)
def num5():
    xdd=21
    while xdd>0:
        xdd=xdd-1
        print(xdd)
def num6():
    fib=int(input("Введите число:"))
    a=0;b=1
    print(a);print(b)
    for i in range(0,fib+1):
        if i==a+b:
            a=b;b=i
            print(i)
def num7():
    s='salam'
    b=''
    for i in range(1,6):
        b+=s[i-1]+str(i)
        print(b)
def num8():
    while True:
        cifra=input('Введите 2 числа через пробел:')
        a,b=cifra.split(' ')
        c=int(a)+int(b)
        print(c)
num8()