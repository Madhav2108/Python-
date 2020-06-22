a=int(input("Enter Days"))

if a>0 and a<=5:
    f=a*40
    print(f," FINE")
elif a>5 and a<=10:
    f=5*40 + (a-5)*65
    print(f," FINE")
else:
    f=5*40 + 5*65 + (a-10)*80
    print(f," FINE")