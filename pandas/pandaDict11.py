import pandas as p
d={'one':p.Series([1,2,3],index=['a','b','c']),'two':p.Series([1,9,3,4],index=['a','b','c','d'])}
data=p.DataFrame(d)
print(data.loc['b'])

