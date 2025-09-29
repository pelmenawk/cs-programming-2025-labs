def num1():
    x = 28
    y= 3,1415
    z = "Пайтон"
    w= False
def num2():
    a= "Кирилл"
    b= '18'
    print(a,b)
def num3():
    a=342
    b= 56.2
    c='43'
    d=(a+b + int(c))
    print(d)
def num4():
    a=3
    b=8
    print((a+4*b)*(a-3*b)+a**2)
def num5():
    a=int(input("сторона1:"))
    b=int(input("сторона2:"))
    print((2*a+2*b),(a*b))
def num6():
    print(' *   *   *')
    print('  * * * *')
    print('   *   *')
def num7():
    x=15
    y=10
    print(f"x*y={x*y};x+y={x+y};x//y={x//y};x-y={x-y};x%y={x%y};x^y={x**y};x/y={x/y}")
    print(f"x=y={x==y};x!=y={x!=y};x>y={x>y};x<y={x<y};x<=y={x<=y};x>=y={x>=y}")
def num8():
    a="Кирилл"
    b="18"
    print(f"Меня зовут {a},мне {b} лет.")
def num9():
    a="Съешь еще "
    b="этих мягких "
    c="французских булок,"
    d="да выпей чаю"
    print(a+b+c+d)
def num10():
    print("Да! Нет!"*4)
def num11():
    a=input()
    x1,x2,x3=a.split(",")
    print(f"Результат вычисления:{(int(x1)+int(x3))//int(x2)}")
def num12():
    a=input()
    print(a[0:4])
    print(a[-2:])
    print(a[3:7])
    print(a[::-1])
num2()