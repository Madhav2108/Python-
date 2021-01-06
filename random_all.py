import random
list=["PYTHON","C++","JAVA",".net"]
for i in range(10):
    print(list[random.randrange(2)],end=",")
    if i%2==0:
        print()
