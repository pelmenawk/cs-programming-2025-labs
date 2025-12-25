def prost(x):
    if x<=1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

cifra=[]
start=int(input("Введите начало диапазона:"))
end=int(input("Введите конец диапазона:"))
for n in range(start,end+1):
    if prost(n):
        cifra.append(n)
if cifra == []:
    print('error')
else:
    print(cifra)