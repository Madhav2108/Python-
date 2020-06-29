import pandas as p
d={'one':p.Series([1,2,5,6],index=['a','b','c','e']),
   'two':p.Series([1,9,3,4],index=['a','b','c','d'])
   }
data=p.DataFrame(d)
print(data[2:4])



