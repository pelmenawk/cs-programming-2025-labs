def num1():
    temp=int(input("Введите температуру:"))
    if temp<20:
        print("Кондиционер включен")
    else:
        print("Кондиционер выключен")
def num2():
    month=int(input("Введите номер месяца:"))
    if 0<month<13:
        if 1<=month<=2 or month==12:
            print("Сейчас зима")
        if 3<=month<=5:
            print("Сейчас весна")
        if 6<=month<=8:
            print("Сейчас лето")
        if 9<=month<=11:
            print("Сейчас осень")
    else:
        print("В году только 12 месяцев")
def num3():
    try:
        sobaka=int(input("Введите возраст вашего собакена:"))
    except ValueError:
        print("Буквы нельзя")
        return
    if sobaka==1 or sobaka ==2:
        print (f"Возраст вашей собаки в человекогодах:{sobaka*10.5}")
    if 3<=sobaka<=22:
        chelovek=(21+(sobaka-2)*4)
        print(f"Возраст вашей собаки в человекогодах:{chelovek}")
    if sobaka<0 or sobaka >22:
        print("Собаке плохо")
def num4():
    a=input("Введите число:")
    b=sum(map(int,list(a)))
    if b%3==0 and int(a)%2==0:
        print("Число кратно 6")
    else:
        print("Число не кратно 6")
def num5():
    a = input('Enter password:')
    b1 = ['1','2','3','4','5','6','7','8','9','0']
    b2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    b3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    b4 = ['`','~','!','@','#','№','$','%','^','&','*','(',')','-','=','+','[',']','{','}','/','<','>',':',';']
    c1 = False
    c2 = False
    c3 = False
    c4 = False
    for i in range(len(a)):
        if a[i] in b1:
            c1 = True
        if a[i] in b2:
            c2 = True
        if a[i] in b3:
            c3 = True
        if a[i] in b4:
            c4 = True
    if len(a)<8:
        print("В пароле меньше 8 символов")
    if c1 == False:
        print('Пароль ненадёжный, отсутствуют цифры')
    if c2 == False:
        print('Пароль ненадёжный, отсутствуют заглавные буквы')
    if c3 == False:
        print('Пароль ненадёжный, отсутствуют строчные буквы')
    if c4 == False:
        print('Пароль ненадёжный, отсутствуют специальные символы')
    if c1 == True and c2 == True and c3 == True and c4 == True:
        print('Пароль надёжный')
def num6():
    god=int(input("Введите год:"))
    if god%4==0 and god%100!=0 or god%400==0:
        print("Год високосный")
    else:
        print("Год не високосный")
def num7():
    a=input("Введите 3 числа через пробел:")
    spisok=[]
    b,c,d=a.split(" ")
    spisok.append(int(b))
    spisok.append(int(c))
    spisok.append(int(d))
    funmin=10000
    funmax=0
    for i in range(3):
        if funmin>spisok[i]:
            funmin=spisok[i]
        if funmax<spisok[i]:
            funmax=spisok[i]
    print(f"Минимальное число-{funmin} ")
    print(f"Максимальное число-{funmax}")
def num8():
    sum=int(input("Введите сумму покупки:"))
    if sum<1000:
        print("Скидки нет")
        print(f"С вас{sum}")
    elif 1000<sum<5000:
        print("Скидка 5%")
        print(f"С вас{sum*0.95}")
    elif 5000<sum<10000:
        print("Скидка 10%")
        print(f"С вас{sum*0.9}")
    elif sum>=10000:
        print("Скидка 15%")
        print(f"С вас {sum*0.85}")
def num9():
    v=int(input("Введите час(целое число от 0-23)"))
    if 0<=v<=5:
        print("Сейчас ночь")
    elif 6<=v<=11:
        print("Сейчас утро")
    elif 12<=v<=17:
        print("Сейчас день")
    elif 18<=v<=23:
        print("Сейчас вечер")
def num10():
    a=input("Введите число:")
    zachem=True
    if a.isdigit():
        a=int(a)
        for i in range(2,a):
            if a==1 or a%i==0:
                zachem=False
        if zachem==True:
            print(f"Число {a}-простое")
        else:
            print(f"Число {a}-составное")
    else:
        print(f"Число {a},стоп,в его числе есть буквы")

num10()