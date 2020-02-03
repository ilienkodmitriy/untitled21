def function1 (a,b):
    import random
    list1 = [random.randint(0,b) for i in range(a)]
    print(list1)
function1(20,100)