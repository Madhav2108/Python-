import pandas as p
l=[['Alex',10],['bob',12],['Clark',13]]
data1=p.DataFrame(l,columns=['NAME','AGE'],dtype=float)
print(data1)