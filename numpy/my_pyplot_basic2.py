import numpy as np
import matplotlib.pyplot as p1
#******************
x=[ 1,2,3, 4,5, 6,7, 8, 9,10]
y=[13,7,2,11,0,17,1,11,22,14]
print(x)
print(y)
p1.xlabel("Overs")
p1.ylabel("Score")
p1.title("IPL 2019")
p1.plot(x,y)
p1.plot(x,y,"ro")
#Player out
p1.plot([4],[11],"b^")
p1.show()
#******************
#******************
a=np.arange(0,10,0.1)
x=np.cos(a)
y=np.sin(a)
print(x)
print(y)
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.plot(a,x,'b',linewidth=10)
p1.plot(a,y,'r',linewidth=2)
p1.show()

#******************
