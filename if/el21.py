a=int(input("Enter Distance"))

if a>0 and a<=20:
    f=a*10
    print(f," FARE")
elif a>20 and a<=40:
    f=200 + (a-20)*7
    print(f," FARE")
else:
    f=200 + 20*7 + (a-40)*6
    print(f," FARE")