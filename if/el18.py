#print(" 1 for area of circle ")
#print(" 2 for area of square ")
#print(" 3 for area of rectangle ")
a=int(input("enter SALE"))
#b=int(input("enter number"))
#c=int(input("enter number"))
#d=int(input("enter number"))
if a<5000:
    d=a*5/100
    t=a-d
    print("AMOUNT ",t)
elif a>5000 and a<=10000:
    d=a*8/100
    t=a-d
    print("AMOUNT ",t)
else:
    d=a*10/100
    t=a-d
    print("AMOUNT ",t)
