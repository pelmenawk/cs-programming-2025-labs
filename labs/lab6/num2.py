vklad=input("Введите сумму вклада(в рублях) и срок(в годах):").split()
a=int(vklad[0])
n=int(vklad[-1])

def income(x,y):
    for i in range(1, y + 1):
        vklad1=0
        shet=x
        while shet>9999 and vklad1<0.05:
            shet-=10000
            vklad1+=0.003
        vklad1 = round(vklad1,4)
        if i <=3:
            vklad1+=0.03
        if 4<=i<=6:
            vklad1+=0.05
        if i>6:
            vklad1+=0.02
        x1 = round(x * (1+vklad1),2)
        x = x1
    print(round(x1 - a,2))
income(a,n)
