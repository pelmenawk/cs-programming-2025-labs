import random
def num1():
    a=[1, 4, 3, 6, 10, 19, 17, 16, 15, 52]
    a[a.index(3)]=30
    print(a)
def num2():
    a=[2,4,6,8,10]
    for i in range(len(a)):
        a[i]=a[i]**2
    print(a)
def num3():
    a=[100,180,88,11,153,16]
    b=max(a)/len(a)
    print(b)
def num4():
    a=19,17,14,100,199
    cnt=0
    for i in a:
        if type(i) is int:
            cnt+=1
    if cnt==len(a):
        b=sorted(a)
        print(b)
    else:
        print(a)
def num5():
    a={"яблоко":100000,"телевизор":22999,"оперативная память":99799}
    minprice=min(a,key=a.get)
    maxprice=max(a,key=a.get)
    print(f"Самый дешевый товар:{minprice}")
    print(f"Самый дорогой товар:{maxprice}")
def num6():
    a=["a","b","c",1,2,3]
    b={}
    for i in a:
        b[i]=i
    print(b)
def num7():
    a={"Tuple":"Кортеж","Lullaby":"Колыбельная","Apple":"Яблоко","Trap":"Ловушка"}
    inp=input("Введите английское слово:")
    if inp in a:
        perevod=a.get(inp)
        print(perevod)
    else:
        print("Такого слова здесь нет")
def num8():
    a=["камень","ножницы","бумага","ящерица","спок"]
    inp=input("Начинайте игру:")
    if inp in a:
        comp=random.choice(a)
        if inp==comp:
            print("Ничья")
        elif inp=="ножницы" and comp=="бумага" or\
        inp=="бумага" and comp=="камень" or\
        inp=="камень" and comp=="ящерица" or\
        inp=="ящерица" and comp=="спок" or\
        inp=="спок" and comp=="ножницы" or\
        inp=="ножницы" and comp=="ящерица" or\
        inp=="ящерица" and comp=="бумага" or\
        inp=="бумага" and comp=="спок" or\
        inp=="спок" and comp=="камень" or\
        inp=="камень" and comp=="бумага":
            print(f"Вы победили,компьютер выбрал:{comp}")
        else:
            print(f"Вы проиграли,компьютер выбрал:{comp}")
        
def num9():
    a=["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]
    b={}
    for fruit in a:
        key=fruit[0]
        if key not in b:
            b[key]=[]
        b[key].append(fruit)
    print(b)
def num10():
    a=[("Анна", [5, 4, 4]), ("Иван", [5, 5, 4]), ("Мария", [5, 3, 5])]
    b={}
    for name,grades in a:
        avg=sum(grades)/len(grades)
        b[name]=avg
    beststudent=max(b,key=b.get)
    bestavg=b[max(b,key=b.get)]
    print(f"Лучший студент {beststudent} с средним баллом {bestavg}")

num8()