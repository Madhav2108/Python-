import os
f=open("gettLIST.txt",'w')
x=["C++","Java","PHP"]
for s in x:
    f.write(s)
    f.write("\n")
f.close()
