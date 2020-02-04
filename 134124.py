def function1(x, y):
    import random
    list1 = [random.randint(0, y) for i in range(y)]
    return list1


a = (int(input("Длина списка: ")))
b = (int(input("Максимальное значение элементов списка: ")))

print(function1(a, b))
