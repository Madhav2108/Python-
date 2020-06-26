class Employee: """'Com m on base class for all em ployees'"""
   empCount = 0
def __init__(self, nam e, salary):
self.nam e = nam e
self.salary = salary
Em ployee.em pCount += 1
def displayCount(self):
print "Total Em ployee %d" % Em ployee.em pCount
def displayEm ployee(self):
print "Nam e : ", self.nam e, ", Salary: ", self.salary
"This would create first object of Em ployee class"
em p1 = Em ployee("Zara", 2000)
"This would create second object of Em ployee class"
em p2 = Em ployee("Manni", 5000)
em p1.displayEm ployee()
em p2.displayEm ployee()
print "Total Em ployee %d" % Em ployee.em pCount
class Em ployee:
'Com m on base class for all em ployees'
em pCount = 0
def __init__(self, nam e, salary):
self.nam e = nam e
self.salary = salary
Em ployee.em pCount += 1
def displayCount(self):
print "Total Em ployee %d" % Em ployee.em pCount
def displayEm ployee(self):
print "Nam e : ", self.nam e, ", Salary: ", self.salary
"This would create first object of Em ployee class"
em p1 = Em ployee("Zara", 2000)
"This would create second object of Em ployee class"
em p2 = Em ployee("Manni", 5000)
em p1.displayEm ployee()
em p2.displayEm ployee()
print "Total Em ployee %d" % Em ployee.em pCount
class Parent: # define parent class
parentAttr = 100
def __init__(self):
print "Calling parent constructor"
def parentMethod(self):
print 'Calling parent m ethod'
def setAttr(self, attr):
Parent.parentAttr = attr
def getAttr(self):
print "Parent attribute :", Parent.parentAttr
class Child(Parent): # define child class
def __init__(self):
print "Calling child constructor"
def childMethod(self):
print 'Calling child m ethod'
c = Child() # instance of child
c.childMethod() # child calls its m ethod
c.parentMethod() # calls parent's m ethod
c.setAttr(200) # again call parent's m ethod
c.getAttr() # again call parent's m ethod
class Parent: # define parent class
def m yMethod(self):
print 'Calling parent m ethod'
class Child(Parent): # define child class
def m yMethod(self):
print 'Calling child m ethod'
c = Child() # instance of child
c.m yMethod() # child calls overridden m ethod
class Vector:
def __init__(self, a, b):
self.a = a
self.b = b
def __str__(self):
return 'Vector (%d, %d)' % (self.a, self.b)
def __add__(self,other):
return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2
#!/usr/bin/python
class JustCounter:
__secretCount = 0
def count(self):
self.__secretCount += 1
print self.__secretCount
counter = JustCounter()
counter.count()
counter.count()
print counter.__secretCount
