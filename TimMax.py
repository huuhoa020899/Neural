from random import randint
def SearchMax():
    n = int(input("Enter n:"))
    a=[]
    for i in range(n):
        a.append(randint(-100,100))
    print (a)
    print (max(a))
SearchMax()