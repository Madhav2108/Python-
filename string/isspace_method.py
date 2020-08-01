s = '   \t'
print(s.isspace())

s = ' a '
print(s.isspace())

s = ''
print(s.isspace())

s = '\t  \n'
if s.isspace() == True:
  print('All whitespace characters')
else:
  print('Contains non-whitespace characters')
  
s = '2+2 = 4'

if s.isspace() == True:
  print('All whitespace characters')
else:
  print('Contains non-whitespace characters.')