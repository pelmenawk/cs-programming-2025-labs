time=input("Введите время и нужную величину в которую нужно его перевести:")    
a,b=time.split(" ")

def perevod(x,y):
    if y[-1]=="h" and y[0]=="m":
        return print(float(x)/60)
    if y[-1]=="m" and y[0]=="h":
        return print(float(x)*60)
    if y[-1]=="s" and y[0]=="h":
        return print(float(x)*3600)
    if y[-1]=="s" and y[0]=="m":
        return print(float(x)*60)
    if y[-1]=="m" and y[0]=="s":
        return print(float(x)/60)
    if y[-1]=="h" and y[0]=="s":
        return print(float(x)/3600)
perevod(a,b)