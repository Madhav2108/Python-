import pandas as p
d={'one':p.Series([1,2,5],index=['a','b','c']),'two':p.Series([1,9,3],index=['a','b','c'])}
data=p.DataFrame(d)
print(data)

print("SUM : \n",data.sum())

print("MIN :\n",data.min())
print("MAX :\n",data.max())

print("MIN INDEX :\n",data.idxmin())
print("MAX INDEX :\n",data.idxmax())

print(data.describe())