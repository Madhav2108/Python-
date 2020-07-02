"""#for
x=3
y=5
for i in range(1,4,2):
    x=x+y
    x=x+2
    y=y+2
    print(x,", ",y)
print(x,",",y)"""
#while:
x=3
y=5
i=1
while i<4:
    x=x+y   #x=8, 17
    x=x+2   #x=10, 19
    y=y+2   #y=7,9
    print(x,", ",y) #10,7   | 19,9
    i=i+2
print(x,",",y) #19,9
#output:
"""
10 ,  7
19 ,  9
19 , 9
"""