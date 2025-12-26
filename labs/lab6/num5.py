def palindrom():
    i=input("Введите строку:")
    a=i.replace(" ","").lower()
    b=a[::-1]
    if a==b:
        print("палиндром!")
    else:
        print("седня не")
palindrom()