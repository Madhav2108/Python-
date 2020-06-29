import matplotlib.pyplot as p

x=[i for i in range(10)]
y=[i*2 for i in x]
p.plot(x,y,'k--')
p.plot(x,y,'go')
p.ylabel('Y RANGE')
p.xlabel('X RANGE')
p.title("THIRD PLOT")
p.show()