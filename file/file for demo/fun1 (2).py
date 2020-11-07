#functions 
#return single value
def dis1(a,b):
   return (a+b)
print(dis1(4,5))
#return multi values value
def dis2(a,b):
   return (a+b),(b-a)
r1,r2=dis2(5,8)
print(r1," , ",r2)
#return multi values value
def dis3(a,b):
   return (a+1),(b-1)
r1,r2=dis3(5,8)
print(r1," , ",r2)
#return multi values value
def dis4(a,b):
   return (a+1),(b-1),(a+b)
r1,r2,r3=dis4(5,8)
print(r1," , ",r2," , ",r3)
#return multi values value
def dis5(a,b):
   return (a+1),(b-1)
a,b=5,2
print("Before :",a," , ",b)
a,b=dis5(a,b)
print("After : ",a," , ",b)
#return multi values value
def dis6(a,b):
   return (b+1),(a-1)
a,b=5,2
print("Before :",a," , ",b)
a,b=dis6(a,b)
print("After : ",a," , ",b)
