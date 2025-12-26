def palindrom():
    i=input("Введите строку:")
    a=i.replace(" ","")
    b=a.lower()
    c=b[::-1]
    if c==b:
        print("палиндром!")
    else:
        print("седня не")
palindrom()