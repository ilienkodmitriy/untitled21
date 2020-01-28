import random
a=(random.randint(0,10))
b=(random.randint(0,10))
c=(random.randint(0,10))
print(a,b,c)

if a>b:
    print("good")
if a<b:
    print("bad")
if a==b:
    print(str(c) + str("Теперь эта!"))
    if (a+b)<c:
        print("very good")
    if (a+b)>c:
        print("very bad")
    if a==b:
        print("suffer")
