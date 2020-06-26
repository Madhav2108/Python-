""" 25.	WAP to print the Income, Tax & Surcharge of Employ. The Tax and Surcharge based on the following conditions
Income				     Tax %		Surcharge
< Rs. 15000			     15%		      7%
Rs. 15001 to Rs. 20000	18% 		     11%
Above Rs. 21000		     20%		      13%
[Total Income =Income- Tax-Surcharge][Tax=Income<Tax_percentage >)/100]display all information like Income, Tax & Surcharge .
"""
i=int(input("enter the value of income:"))
tax=0
surcharge=0
if i<15000:
     tax=15
     surcharge=7
elif i<15001 and i>20000:
     tax=18
     surcharge=11
elif i<21000:
     tax=20
     surcharge=13
else:
     tax=12
     surcharge=18
     total_amount=i-tax-surcharge
     tax=i/100*tax
     print("income is",i)
     print("tax is",tax)
     print("surcharge is",surcharge)


