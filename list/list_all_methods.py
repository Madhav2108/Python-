List1=["Python",12,"and",11,[1,2,5,7],"Programming"]
List2=[12,32,33]
print("1 List1: ",List1)
print("2 len(List1)             : ",len(List1))
print("3 List1.count(item)      : ",List1.count(11))
print("4 List1(Index/POS)       : ",List1[4])
print("5 List1[Start:End]/Range : ",List1[2:4])
List3=List2.copy()
print("6 List2                  : ",List2)
print("7 List3                  : ",List3)
print("8 min(List1)             : ",min(List2))
print("9 max(List1)             : ",max(List2))
print("10 sorted(List1)         : ",sorted(List2))
#List1.reverse()        
List2.reverse()
print("1 List2: ",List2)
print("2 List1.pop(Index/POS)   : ",List1.pop(2));
#List1.remove(Item)
List1.remove(12)
print("3 List1: ",List1)
#List.append(Item)
List1.append(241)
print("4 List1: ",List1)
#List.insert(POS,Item)
List1.insert(1,71)
print("5 List1: ",List1)
#print("List.extend(LIST)
List1.extend(List2)
print("6 List1 :",List1)
#del List1[POS/Index/Range like[Start : End]]
del List1[1]
print("7 List ",List1)

"""
1 List1:  ['Python', 12, 'and', 11, [1, 2, 5, 7], 'Programming']
2 len(List1)             :  6
3 List1.count(item)      :  1
4 List1(Index/POS)       :  [1, 2, 5, 7]
5 List1[Start:End]/Range :  ['and', 11]
6 List2                  :  [12, 32, 33]
7 List3                  :  [12, 32, 33]
8 min(List1)             :  12
9 max(List1)             :  33
10 sorted(List1)          :  [12, 32, 33]
1 List2:  [33, 32, 12]
2 List1.pop(Index/POS)   :  and
3 List1:  ['Python', 11, [1, 2, 5, 7], 'Programming']
4 List1:  ['Python', 11, [1, 2, 5, 7], 'Programming', 241]
5 List1:  ['Python', 71, 11, [1, 2, 5, 7], 'Programming', 241]
6 List1 : ['Python', 71, 11, [1, 2, 5, 7], 'Programming', 241, 33, 32, 12]
7 List  ['Python', 11, [1, 2, 5, 7], 'Programming', 241, 33, 32, 12]
"""
