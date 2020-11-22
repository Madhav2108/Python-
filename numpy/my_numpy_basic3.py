import numpy as np
x =np.arange(0.0,5.0,1.0)
print(np.savetxt('test.out', x, delimiter=','))
# Initialize `x`
x = np.ones((3,4))
# Check shape of `x`
print(x.shape)
print(x )
# Initialize `y`
y = np.arange(4)
# Check shape of `y`
print(y.shape)
print(y )
# Subtract `x` and `y`
print(x - y)
print(x + y)
print(x *y)


#*****************************
a = np.array([1, 2, 5, 3]) 
  
# add 1 to every element 
print ("Adding 1 to every element:", a+1) 
  
# subtract 3 from each element 
print ("Subtracting 3 from each element:", a-3) 
  
# multiply each element by 10 
print ("Multiplying each element by 10:", a*10) 
  
# square each element 
print ("Squaring each element:", a**2) 
  
# modify existing array 
a *= 2
print ("Doubled each element of original array:", a) 
  
# transpose of array 
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]]) 
  
print ("\nOriginal array:\n", a) 
print ("Transpose of array:\n", a.T)

#*********************************************
arr = np.array([[1, 5, 6], 
                [4, 7, 2], 
                [3, 1, 9]]) 
  
# maximum element of array 
print ("Largest element is:", arr.max()) 
print ("Row-wise maximum elements:", 
                    arr.max(axis = 1)) 
  
# minimum element of array 
print ("Column-wise minimum elements:", 
                        arr.min(axis = 0)) 
  
# sum of array elements 
print ("Sum of all array elements:", 
                            arr.sum()) 
  
# cumulative sum along each row 
print ("Cumulative sum along each row:\n", 
                        arr.cumsum(axis = 1)) 
#***********************************************
#binary operator
a = np.array([[1, 2], 
            [3, 4]]) 
b = np.array([[4, 3], 
            [2, 1]]) 
  
# add arrays 
print ("Array sum:\n", a + b) 
  
# multiply arrays (elementwise multiplication) 
print ("Array multiplication:\n", a*b) 
  
# matrix multiplication 
print ("Matrix multiplication:\n", a.dot(b)) 
