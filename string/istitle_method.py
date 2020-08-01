s = 'Python Is Good.'
print(s.istitle())

s = 'Python is good'
print(s.istitle())

s = 'This Is @ Symbol.'
print(s.istitle())

s = '99 Is A Number'
print(s.istitle())

s = 'PYTHON'
print(s.istitle())

s = 'I Love Python.'
if s.istitle() == True:
  print('Titlecased String')
else:
  print('Not a Titlecased String')
  
s = 'PYthon'
if s.istitle() == True:
  print('Titlecased String')
else:
  print('Not a Titlecased String')