from random import randint as ri

a = (int(input("Длина списка: ")))
b = (int(input("Максимальное значение элементов списка: ")))
c = (int(input("Длина списка: ")))
d = (int(input("Максимальное значение элементов списка: ")))

def func(x, y, w, z):
    list1 = []
    for i in range(x):
        list1.append(ri(0, y))
    list2 = []
    for e in range(w):
        list2.append(ri(0, z))
    list3 = []
    for s in list1:
        if s in list2:
            list3.append(s)
    if len(list3) == 0:
        print("Совпадений нет!")
        return list3
    else:
        return list(set(list3))

print(func(a, b, c, d))
