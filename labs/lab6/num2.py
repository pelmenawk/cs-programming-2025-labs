vklad=input("Введите сумму вклада(в рублях) и срок(в годах):").split(" ")
a=int(vklad[0])
n=int(vklad[-1])

def income(x,y):
    vklad1=0
    shet=x-30000
    while shet>10000 and vklad1<0.05:
        shet-=10000
        vklad1+=0.003
    srokstav=0
    if y <=3:
        srokstav==0.03
    if 4<=y<=6:
        srokstav==0.05
    if y>6:
        srokstav==0.02
    vsestav=vklad1+srokstav
    for i in range(n):
        x1=x*(1+vsestav)
    x2=x1-x
    print(x2)
income(a,n)
