def GiaiPhuongTrinh(a,b):
    #a = int(input("Enter number A:"))
            
    #b = int(input("Enter number B:"))
    if a==0:
       if b==0:
            msg="Phuong trinh vo so nghiem"
       else:
           msg="Phuong trinh vo nghiem."
    else:
        x=-b/a
        msg="Nghiem cua phuong trinh %f"%(x)
#GiaiPhuongTrinh()
