import numpy as np
import matplotlib.pyplot as p1
x=np.arange(7)
y=np.arange(1,20,3)
print(x)
print(y)
p1.plot(x,y)
p1.show()
#******************
x=np.arange(7)
y=np.arange(1,20,3)
print(x)
print(y)
p1.xlabel("Data from list x")
p1.ylabel("Data from list y")
p1.title("My PyPlot 1")
p1.plot(x,y)
p1.show()
#******************
x=[ 1,2,3, 4,5, 6,7, 8, 9,10]
y=[13,7,2,11,0,17,1,11,22,14]
print(x)
print(y)
p1.xlabel("Overs")
p1.ylabel("Score")
p1.title("IPL 2019")
p1.plot(x,y)
p1.show()
#******************
x=[1,2,3,4,5,6,7,8,9,10]
y=[13,7,2,11,0,17,1,11,22,14]
print(x)
print(y)
p1.xlabel("Overs")
p1.ylabel("Score")
p1.title("IPL 2019")
p1.plot(x,y,'y')
p1.plot(x,y,"r^")
p1.show()
#******************
