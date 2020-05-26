def KTSNT():
    x=int(input ("enter x:"))
    dem =0
    for i in range(1,x+1):
        if x % int( i) == 0:
            dem=dem+1;
        if dem>2:
            break
    if dem==2:
        print("N la so nguyen to")
    else:
        print (" N k la so nguyen to")
KTSNT()