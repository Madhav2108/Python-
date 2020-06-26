#print(" 1 for area of circle ")
#print(" 2 for area of square ")
#print(" 3 for area of rectangle ")
a=int(input("enter INCOME"))
#b=int(input("enter number"))
#c=int(input("enter number"))
#d=int(input("enter number"))
if a<15000:
    t=a*15/100
    s=a*7/100
    i=a-t-s
    print("FINAL INCOME ",i)
elif a>15000 and a<=20000:
    t=a*18/100
    s=a*11/100
    i=a-t-s
    print("FINAL INCOME ",i)
else:
    t=a*20/100
    s=a*13/100
    i=a-t-s
    print("FINAL INCOME ",i)

