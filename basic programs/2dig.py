#Set 4
print ("#1.	WAP to display factors of a given number till N.")
N=int(input("Enter Any Number: "))
print ("All Factors: \n")
for i in range(1,N+1,1):
    if(N%i==0):
        print(i)
print ("#2.	WAP to display Even factors of a given number till N.")
print ("Even Factors: \n")
for i in range(1,N+1,1):
    if(N%i==0):
        if i%2==0:
            print(i)
print ("#3.	WAP to display odd factors of a given number till N.")
print ("Odd Factors: \n")
for i in range(1,N+1,1):
    if(N%i==0):
        if i%2!=0:
            print(i)
print ("Even and Factors in single line : \n")
for i in range(1,N+1,1):
    if(N%i==0)and (i%2==0):
        print(i)
print ("#4.	WAP to display factorial of a given numbers.")
N=int(input("Enter Any Number: "))
F=1
for i in range(1,N+1,1):
   F=F*i
print("The factorial of ",N ," is ",F)
print ("#5.	WAP to check given number is prime or not")
N=int(input("Enter Any Number: "))
c=0
for i in range(1,N+1,1):
   if N%i==0:
       c=c+1
if c==2:
   print("The Number ",N ," is Prime")
else:
   print("The Number ",N ," is Prime")
print ("#6.	WAP to display all prime numbers from N to M.")
N=int(input("Enter Any Number N: "))
M=int(input("Enter Any Number M: "))
c=0
for i in range(N,M+1,1):
    c=0
    for j in range(1,i+1,1):
       if i%j==0:
          c=c+1
    if c==2:
      print("The Number ",i ," is Prime")
print ("#7.	WAP to check given two number are twin prime or not")
N=int(input("Enter Any Number N: "))
M=int(input("Enter Any Number M: "))
c1=0
c2=0
for i in range(1,N+1,1):
   if N%i==0:
       c1=c1+1
for i in range(1,M+1,1):
   if M%i==0:
       c2=c2+1
if c1==2 and c2==2:
    if N-M==2 or N-M==-2:
        print("Number are twin prime")
    else:
        print("Number are not twin prime")
print ("#8.	WAP to check given numbers is perfect no or not.")
N=int(input("Enter Any Number N: "))
s=0
for i in range(1,N+1,1):
   if N%i==0:
       s=s+i
if s==N:
    print(N," is perfect no")
else:
    print(N," is not perfect no")
"""
#1.	WAP to display factors of a given number till N.
Enter Any Number: 13
All Factors: 

1
13
#2.	WAP to display Even factors of a given number till N.
Even Factors: 

#3.	WAP to display odd factors of a given number till N.
Odd Factors: 

1
13
Even and Factors in single line : 

#4.	WAP to display factorial of a given numbers.
Enter Any Number: 5
The factorial of  5  is  120
#5.	WAP to check given number is prime or not
Enter Any Number: 13
The Number  13  is Prime
#6.	WAP to display all prime numbers from N to M.
Enter Any Number N: 12
Enter Any Number M: 33
The Number  13  is Prime
The Number  17  is Prime
The Number  19  is Prime
The Number  23  is Prime
The Number  29  is Prime
The Number  31  is Prime
#7.	WAP to check given two number are twin prime or not
Enter Any Number N: 11
Enter Any Number M: 13
Number are twin prime
#8.	WAP to check given numbers is perfect no or not.
Enter Any Number N: 6
6  is not perfect no
"""




       
