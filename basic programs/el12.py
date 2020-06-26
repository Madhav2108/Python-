a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
d=int(input("enter number"))
if a<b and a<c and a<d:
    print(a," LOWEST")
elif b<c and b<a and b<d:
    print(b," LOWEST")
elif c<a and c<b and c<d:
    print(c," LOWEST")
else:
    print(d," LOWEST")                                                               
