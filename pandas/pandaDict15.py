import pandas as p

d1=p.DataFrame([[1,2],[3,4]],columns=['a','b'])
d2=p.DataFrame([[5,6],[7,8]],columns=['a','b'])
d1=d1.append(d2)
print(d1)

d1=d1.drop(0)
print(d1)