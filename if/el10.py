a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
d=int(input("enter number"))
if a>b and a>c and a>d:
    print(a," Greater")
elif b>c and b>a and b>d:
    print(b," Greater")
elif c>a and c>b and c>d:
    print(c," Greater")
else:
    print(d," Greater")                                                               
