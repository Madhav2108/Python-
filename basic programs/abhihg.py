s=int(input("enter value of sale:"))
discount=0
subcharge=0
if s<5000:
    discount=5
    subcharge=5 
elif s>5000 and s<10000:
    discount=10
    subcharge=15
else:
    discount=15
    subcharge=20
    dc=s/100*discount
    total=s-dc
    print("amount is",s)
    print("discount is ",dc)
    print("subcharge is ",subcharge)
    print("total amount is ",total)
