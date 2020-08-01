# example string
string = "THIS IS GOOD!"
print(string.isupper());

# numbers in place of alphabets
string = "THIS IS ALSO G00D!"
print(string.isupper());

# lowercase string
string = "THIS IS not GOOD!"
print(string.isupper());

string = 'THIS IS GOOD'
if string.isupper() == True:
  print('Does not contain lowercase letter.')
else:
  print('Contains lowercase letter.')
  
string = 'THIS IS gOOD'
if string.isupper() == True:
  print('Does not contain lowercase letter.')
else:
  print('Contains lowercase letter.')