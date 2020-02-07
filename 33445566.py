from random import randint as ri

userString = (str(input("Введите данные:")))

def func (x,y,z):
    result = {x:ri(y,z)}
    return result

print (func(userString,0,10000))