size = input('Введите размерность матрицы:').split()
n1 = int(size[0])
n2 = int(size[-1])
a = []
b = []
c = []
for i in range(n1):
    a.append(input("введите строку первой матрицы:").split())
for i in range(n1):
    b.append(input("введите строку второй матрицы:").split())


for n in range(len(b)):
    for x in range(len(a[n])):
        c.append(int(a[n][x])+int(b[n][x]))






