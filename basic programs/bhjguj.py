"""24.	WAP to print the Discount in Rupees for a salesman. The Discount is based on the following conditions
Sales				Dis %
< Rs. 5000			5%
Rs. 5000 to Rs. 10000		8%
Above Rs. 10000		10%
[Dis=Sales*<Dis_percentage >)/100] ,[Total Amount=Sales-Dis]
"""
s=int(input ("enter value of sale:"))
discount=0
if s<5000:
    discount=5
elif s<5000 and s<10000:
    discount=8
else:
    discount=10
    dc=s/100*dis
    ta=s-dc
    print("amount is",s)
    print("discount is",dc)
    print("total amount is",ta)
