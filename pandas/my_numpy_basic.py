import numpy as np
#1D
L=[1,2,3,4]
print(L)            #[1, 2, 3, 4]
print(np.array(L))  #[1 2 3 4]
a=np.array(L)       
print(a)            #[1 2 3 4]
print(a.shape)      #(4,)
print(a.itemsize)   #4
print(a.strides)    #(4,)
#2D
L=[[1,2,3,4],[4,6,13,9]]
print(L)            #[[1, 2, 3, 4], [4, 6, 13, 9]]
print(np.array(L))  #[[ 1  2  3  4]
                    # [4  6 13  9]]
a=np.array(L)       
print(a)            #[[ 1  2  3  4]
                    # [ 4  6 13  9]]
print(a.shape)      #(2, 4)
print(a.itemsize)   #4
#print(a.strides)    #(16, 4)
#1D assign 
a=np.arange(7)  
print(a)            #[0 1 2 3 4 5 6]
a=np.arange(1,17,5)
print(a)            #[ 1  6 11 16]
a=np.linspace(2.5,17,6)
print(a)            #[ 2.5   9.75 17.  ]


