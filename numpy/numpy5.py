import numpy as np 

dt = np.dtype([('age',np.int8)]) 
a = np.array([(10.2,),(20,),(30,)], dtype = dt) 
print (a)

print(a['age'])