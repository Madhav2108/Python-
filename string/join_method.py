numList = ['1', '2', '3', '4']
seperator = ', '
print(seperator.join(numList))

numTuple = ('1', '2', '3', '4')
print(seperator.join(numTuple))

s1 = 'abc'
s2 = '123'

""" Each character of s2 is concatenated to the front of s1""" 
print('s1.join(s2):', s1.join(s2))

""" Each character of s1 is concatenated to the front of s2""" 
print('s2.join(s1):', s2.join(s1))

test =  {'2', '1', '3'}
s = ', '
print(s.join(test))

test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))

test =  {'mat': 1, 'that': 2}
s = '->'
print(s.join(test))

test =  {1:'mat', 2:'that'}
s = ', '

# this gives error
print(s.join(test))