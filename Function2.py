def func(a,b,c,d):
    import random
    list1 = [random.randint(0, b) for i in range(a)]
    list2 = [random.randint(0, d) for i in range(c)]
    print(list1, list2)
    list3 = list(set(list1) & set(list2))
    print(list3)
    if list3 == []:
        print("совпадений нет")
func(19,27,5,30)