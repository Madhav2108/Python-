print(" 1 for area of circle ")
print(" 2 for area of square ")
print(" 3 for area of rectangle ")
a=int(input("enter OPTION"))
#b=int(input("enter number"))
#c=int(input("enter number"))
#d=int(input("enter number"))
if a==1:
    r=int(input("Enter Radius"))
    ar=3.14*r*r
    print(ar," Area of Circle") 
elif a==2:
    s=int(input("Enter side"))
    ar=s*s
    print(ar," Area of Square")
elif a==3:
    l=int(input(" Length"))
    b=int(input(" Breadth"))
    ar=l*b
    print(ar," Area of Rectangle")
else:
    print("INVALID")
