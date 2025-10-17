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