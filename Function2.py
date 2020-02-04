a = (int(input("Введіть бажану довжину першого списку та натисніть Enter: ")))
b = (int(input("Максимальное значение элементов списка: ")))
c = (int(input("Введіть бажану довжину другого списку та натисніть Enter: ")))
d = (int(input("Максимальное значение элементов списка: ")))

def func(a,b,c,d):
    import random
    list1 = [random.randint(0, b) for i in range(a)]
    list2 = [random.randint(0, d) for i in range(c)]
    list3 = list(set(list1) & set(list2))
        print(list3)
        if list3 == []:
            print("совпадений net")

print (listFunc2(a,b,c,d))



