import pandas as p
d=[{'a':1,'b':2,'c':3},{'a':5,'b':10,'c':20}]
data=p.DataFrame(d,index=['first','second'],columns=['a','b1'])
print(data)
data=p.DataFrame(d,index=['first','second'],columns=['a','b'])
print(data)
