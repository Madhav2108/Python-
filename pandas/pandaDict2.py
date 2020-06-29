import pandas as p
d={'NAME':['Tom','Jack','Steve','Ricky'],'AGE':[28,34,29,42]}
data=p.DataFrame(d,index=['rank1','rank2','rank3','rank4'])
print(data)