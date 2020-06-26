a=int(input("Enter value of  a: "))
b=int(input("Enter value of  b: "))
c=int(input("Enter value of  c: "))
if a>b and a>c:
    print(a," is Greater then ",b," and",c)
elif b>a and b>c:
   print(b," is Greater then ",a," and",c)
else:
    print(c," is Greater then ",a," and",b)