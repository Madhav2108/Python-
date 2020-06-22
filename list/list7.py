print("Program :7 :")
# *number : number of time List.
list1=[1, 3, 5]
print(list1*2)
# Display List
list1= ['Data Structure', 'C', 'C++', 'Java', 'Unix', 'DBMS', 'Python', 'SQL', 'IBM', 'Microsoft', 'Apple']
print("Orignal list is ",list1)
for data in list1:
       print(data)
#count():Calculates total occurrence of given element of List.
list1=[1, 3, 5, 7, 17, 9, 19, 7, 113, 7, 121, 7]
print("Orignal list is ",list1)
c=list1.count(7)
print(7," comes ",c, " times")  #4
#length: Calculates total length of List.Syntax: len(list_name)
list1=[1, 3, 5, 7, 17, 9, 19, 7, 113, 7, 121, 7]
print("Orignal list is ",list1)
print("Number of items in list : ",len(list1)) #12
#sort() and reverse() 
list1.sort()
print("Orignal list is ",list1)
list1.reverse()
print("list After Reverse:  ",list1) #[121, 113, 19, 17, 9, 7, 7, 7, 7, 5, 3, 1]
#Deletion of List Elements:list.pop([index])
print(list1)#[121, 113, 19, 17, 9, 7, 7, 7, 7, 5, 3, 1]
list1.pop(4)
print("Orignal list is ",list1)#[121, 113, 19, 17, 7, 7, 7, 7, 5, 3, 1]
print("The Element is ",list1.pop(0))#121

#Elegant way to create new List
pow1= [2 ** x for x in range(10) ]
print(pow1)
#Elegant way to create new List
pow2 = []
for x in range(10):
   pow2.append(2 ** x)
print(pow2)
#Elegant way to create new List
print("List: ",end="")
for i in pow2:
    print(i,end=", ")
