matrix=input("Введите размерность матрицы через пробел:").split()
n1=int(matrix[0])
n2=int(matrix[-1])
if n1!=n2 or n1<=2 or n2<=2:
    print("ерор размерности")
else:
    a=[]
    b=[]
    c=[]
    for i in range(n1):
        a.append(input("введите строку первой матрицы:").split())
    for i in range(n1):
        b.append(input("введите строку второй матрицы:").split())


    for n in range(len(b)):
        for x in range(len(a[n])):
            c.append(int(a[n][x])+int(b[n][x]))
print(c)