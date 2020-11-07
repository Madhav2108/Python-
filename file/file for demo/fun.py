def sum(*n):
    total=0
    for i in n:
        print(i,end=", ")
        total=total+i
    print("The sum is : ",total)
sum()
sum(20)
sum(20,30)
sum(10,20,30,40)