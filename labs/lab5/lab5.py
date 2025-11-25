def num9():
    a=["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]
    b={}
    for fruit in a:
        key=fruit[0]
        if key not in b:
            b[key]=[]
        b[key].append(fruit)
    print(b)
num9()