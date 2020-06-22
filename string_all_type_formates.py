str = "This is me rakesh"
n = len(str)
print('Length of string is : ',n)
str = str + "Hello rakesh"
print(str)
print(str[0])
#************************************
str = "This is original string"
rev = ''.join(reversed(str))
print(rev)
#************************************
#String Length:
s="Python Programming"
print("The String is:",s)
print("The String Length is :",len(s))
#************************************
str="Python is Fun"
print("*".join(str))
print("*".join((str," hello ",str)))
print(str.split(" "))
print(str.replace("s","k"))
#************************************
s="Gajendra"
print(s)
print(s[5])
print(s[-5])
m="Sharma"
print(s+" "+m)
print(s[0]+" "+m[1])
#************************************
str ="it is not easy to play another man's game" 
print (str )
str1="man" 
str2= "woman" 
print (str.find(str1)) 
print (str.find(str2)) 
#************************************
str ="it is not easy to play another man's game" 
print (str )
str1="man" 
str2= "woman" 
print (str.find(str1)) 
print (str.find(str2)) 
#************************************
str ="it is not easy to play another man's game" 
sub = "is" 
print (str.endswith(sub,2,5))
print (str.endswith(sub,30) )
sub = "game" 
print (str.endswith(sub) )
#************************************
str = "This is a count example sss"
sub = "i" 
print ("1: ",str.count(sub, 4, len (str)))
sub = "a" 
print ("2: ",str.count(sub,10))
sub = "a" 
print ("3: ",str.count(sub)) 
sub = "s" 
print ("4: ",str.count(sub,9)) 
#************************************
str="Python for All type of Design"
print(str)
print(str.endswith("a"))
print(str.endswith("n"))
print(str.find("n"))
print(str.find("o"))
print(str.find("of"))
str1="Aman23"
print(str1.isalnum())
print(str1.isalpha())
str2="123@"
print(str2.isdigit())
str3="123"
print(str3.isdigit())
#************************************
str = '''   Python has a built-in string class named "str" with many handy 
        features (there is an older module named "string" which you
         should not use Python. String literals can be enclosed
         by either double or single quotes, 
         although single quotes are more commonly used   '''
print("String length :", len(str))   
upper = str.upper()      
print("String in upper case : ")
print(upper)
lower = upper.lower()
print("\n\nString in lower case :", lower)
strip = str.strip()
print("\n\nString without space at begining and end :", strip)
startwith = str.startswith('python')  #return true or fals
endwith   = str.endswith('hello')
print(startwith)
print(endwith)
find = str.find('quotes')  # display the index of first occurance of the string
print("First appeared at :",find)
newstr = str.replace('Python','c++')
print("\n\n New string where 'Python' was replaced with 'C++' \n", newstr)
split = str.split(' ')  # return result in a list
print(split)


#************************************

a="Python"
b="JAVA"
c="C++"
#a,b,c="Python","JAVA","C++"
#a,b,c="PYTHON"
print(a)# Output:Python
print(a*3)# Output:PythonPythonPython
print("%s"%a)# Output:Python
print ("Lang1 is %s ,Lang2 is %s Lang3  is %s" % (a,b,c)) #output:Lang1 is Python ,Lang2 is JAVA Lang3  is C++
print("{},{},{}".format(a,b,c))# Output:Python,JAVA,C++
print("{1},{2},{0}".format(a,b,c))# Output:JAVA,C++,Python
print("{2},{0},{1}".format(a,b,c))# Output:C++,Python,JAVA
print('Hello {lang1}, {lang2}'.format(lang1 = 'C++', lang2= 'JAVA'))# Output:Hello C++, JAVA
print('Hello {lang2}, {lang1}'.format(lang1 = 'C++', lang2= 'JAVA'))# Output:Hello JAVA, C++
print(1,2,3,4)# Output: 1 2 3 4
print(1,2,3,4,sep='*')# Output: 1*2*3*4
print(1,2,3,4,sep='#',end='&')#Output: 1#2#3#4&
print()
t=(5,8,3,9)
print(t,sep='#',end='&')#Output: (5, 8, 3, 9)&
print() 
str="""Strings are amongst the most popular types in Python."""
print(str)
#************************************
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("The String is:",s)
#Pro1  Slicing or Substrings
#String Name [index Position]-ve or +ve:
print ("s[2]    : ", s[2])
print ("s[-2]    : ", s[-2])
print ("s[2: ]  : ", s[5:])
print ("s[2:9] : ", s[2:16])
#display by user choice:
pos=int(input("Enter position: "))
print ("s[",pos,"] : ", s[pos])
#Updating Strings  or add more data:
s="Ravi"
print(s)
s=s+"Kumar" #s=s+" Kumar"
print(s)
#Strings  str.center(width[, fillchar] ) :
str = "Germany won the FIFA CUP" 
str1= str.center(30,'a') 
str2= str.center(30)
#Strings  str.count(substr [, start [, end]]):
print (str1 )
print (str2)
s = "Ths is a count example"
sub = "i" 
print (s.count(sub, 4, len (str)))
sub = "a" 
print (s.count(sub) )
#Strings  str.endswith(suffix[, start[, end]]) :
s ="it is not easy to play another man's game" 
sub = "is" 
print (s.endswith(sub,2,5))
print (s.endswith(sub,30) )
sub = "game" 
print (s.endswith(sub) )
#Strings  str.find(str, beg=0 end=len(string))  :
s ="it is not easy to play another man's game" 
print (s)
print ("\n" )
str1="man" 
str2= "woman" 
print (s.find(str1) )
print (s.find(str2) )
#************************************
str="Python for All type of Design"
print(str) #Python for  All type of Design
print(str[3]) # h
print(str[3:10]) #hon for 
print(str[5:]) #n for  All type of Design
print(str[-3]) #i
print(len(str)) #29
#************************************
str="sAy To hEllo PyThon"
print(str)
print(str.islower() )
print(str.isspace() )
print(str.istitle() )
print(str.lower() )
print(str.upper() )
print(str.title() )
print(str.swapcase() )
print(str.replace("To","from" ))
print(str.center(30,"*"))
#************************************
string = "PYTHON IS AWESOME"
# print lowercase string
print("Lowercase string:", string.casefold())
string = "PYTHON IS AWESOME"
# print lowercase string
print("Lowercase string:", string.casefold())
firstString = "der Fluß"
secondString = "der Flusss"
# ß is equivalent to ss
if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')
string = "Python is awesome"
new_string = string.center(27,'*')
print("Centered String: ", new_string)
string = "Python is awesome"
new_string = string.center(24)
print("Centered String: ", new_string)
string = "Python is awesome, isn't it?"
substring = "is"
count = string.count(substring)
# print count
print("The count is:", count)
# define string
string = "Python is awesome, isn't it?"
substring = "i"
# count after first 'i' and before the last 'i'
count = string.count(substring, 8, 25)
# print count
print("The count is:", count)
# unicode string
string = 'pythön!'
# print string
print('The string is:', string)
# default encoding to utf-8
string_utf = string.encode()
# print result
print('The encoded version is:', string_utf)
# unicode string
string = 'pythön!'
# print string
print('The string is:', string)
# ignore error
print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))
# replace error
print('The encoded version (with replace) is:', string.encode("ascii", "replace"))
text = "Python is easy to learn."
result = text.endswith('to learn')
# returns False
print(result)
result = text.endswith('to learn.')
# returns True
print(result)
result = text.endswith('Python is easy to learn.')
# returns True
print(result)
text = "Python programming is easy to learn."

# start parameter: 7
# "programming is easy to learn." string is searched
result = text.endswith('learn.', 7)
print(result)

# Both start and end is provided
# start: 7, end: 26
# "programming is easy" string is searched

result = text.endswith('is', 7, 26)
# Returns False
print(result)

result = text.endswith('easy', 7, 26)
# returns True
print(result)
str = 'xyz\t12345\tabc'

# no argument is passed
# default tabsize is 8
result = str.expandtabs()

print(result)
str = "xyz\t12345\tabc"
print('Original String:', str)

# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))

# tabsize is set to 3
print('Tabsize 3:', str.expandtabs(3))

# tabsize is set to 4
print('Tabsize 4:', str.expandtabs(4))

# tabsize is set to 5
print('Tabsize 5:', str.expandtabs(5))

# tabsize is set to 6
print('Tabsize 6:', str.expandtabs(6))
quote = 'Let it be, let it be, let it be'

result = quote.find('let it')
print("Substring 'let it':", result)

result = quote.find('small')
print("Substring 'small ':", result)

# How to use find()
if  (quote.find('be,') != -1):
  print("Contains substring 'be,'")
else:
  print("Doesn't contain substring")
quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))

# Substring is searched in ' small things with great love' 
print(quote.find('small things', 2))

# Substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))
# default arguments
print("Hello {}, your balance is {}.".format("Adam", 230.2346))

# positional arguments
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))

# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))
# integer arguments
print("The number is:{:d}".format(123))

# float arguments
print("The float number is:{:f}".format(123.4567898))

# octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))
# integer numbers with minimum width
print("{:5d}".format(12))

# width doesn't work for numbers longer than padding
print("{:2d}".format(1234))

# padding for float numbers
print("{:8.3f}".format(12.2346))

# integer numbers with minimum width filled with zeros
print("{:05d}".format(12))

# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))
# show the + sign
print("{:+f} {:+f}".format(12.23, -12.23))

# show the - sign only
print("{:-f} {:-f}".format(12.23, -12.23))

# show space for + sign
# integer numbers with right alignment
print("{:5d}".format(12))

# float numbers with center alignment
print("{:^10.3f}".format(12.2346))

# integer left alignment filled with zeros
print("{:<05d}".format(12))

# float numbers with center alignment
print("{:=8.3f}".format(-12.2346))
# integer numbers with right alignment
print("{:5d}".format(12))

# float numbers with center alignment
print("{:^10.3f}".format(12.2346))

# integer left alignment filled with zeros
print("{:<05d}".format(12))

# float numbers with center alignment
print("{:=8.3f}".format(-12.2346))
# string padding with left alignment
print("{:5}".format("cat"))

# string padding with right alignment
print("{:>5}".format("cat"))

# string padding with center alignment
print("{:^5}".format("cat"))

# string padding with center alignment
# and '*' padding character
print("{:*^5}".format("cat"))
# truncating strings to 3 letters
print("{:.3}".format("caterpillar"))

# truncating strings to 3 letters
# and padding
print("{:5.3}".format("caterpillar"))

# truncating strings to 3 letters,
# padding and center alignment
print("{:^5.3}".format("caterpillar"))
# define Person class
class Person:
    age = 23
    name = "Adam"

# format age
print("{p.name}'s age is: {p.age}".format(p=Person()))
# define Person dictionary
person = {'age': 23, 'name': 'Adam'}

# format age
print("{p[name]}'s age is: {p[age]}".format(p=person))
# dynamic string format template
string = "{:{fill}{align}{width}}"

# passing format codes as arguments
print(string.format('cat', fill='*', align='^', width=5))

# dynamic float format template
num = "{:{align}{width}.{precision}f}"

# passing format codes as arguments
print(num.format(123.236, align='<', width=8, precision=2))

sentence = 'Python programming is fun.'

result = sentence.index('is fun')
print("Substring 'is fun':", result)

result = sentence.index('Java')
print("Substring 'Java':", result)
sentence = 'Python programming is fun.'

# Substring is searched in 'gramming is fun.'
print(sentence.index('ing', 10))

# Substring is searched in 'gramming is '
print(sentence.index('g is', 10, -4))

# Substring is searched in 'programming'
print(sentence.index('fun', 7, 18))
name = "M234onica"
print(name.isalnum())

# contains whitespace
name = "M3onica Gell22er "
print(name.isalnum())

name = "Mo3nicaGell22er"
print(name.isalnum())

name = "133"
print(name.isalnum())

name = "M0n1caG3ll3r"

if name.isalnum() == True:
   print("All characters of string (name) are alphanumeric.")
else:
    print("All characters are not alphanumeric.")
name = "Monica"
print(name.isalpha())

# contains whitespace
name = "Monica Geller"
print(name.isalpha())

# contains number
name = "Mo3nicaGell22er"
print(name.isalpha())
s = "28212"
print(s.isdecimal())

# contains alphabets
s = "32ladk3"
print(s.isdecimal())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdecimal())
s = "28212"
print(s.isdigit())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdigit())
str = 'Python'
print(str.isidentifier())

str = 'Py thon'
print(str.isidentifier())

str = '22Python'
print(str.isidentifier())

str = ''
print(str.isidentifier())

str = 'root33'
if str.isidentifier() == True:
  print(str, 'is a valid identifier.')
else:
  print(str, 'is not a valid identifier.')
  
str = '33root'
if str.isidentifier() == True:
  print(str, 'is a valid identifier.')
else:
  print(str, 'is not a valid identifier.')
  
str = 'root 33'
if str.isidentifier() == True:
  print(str, 'is a valid identifier.')
else:
  print(str, 'is not a valid identifier.')
s = 'this is good'
print(s.islower())

s = 'th!s is a1so g00d'
print(s.islower())

s = 'this is Not good'
print(s.islower())

s = 'this is good'
if s.islower() == True:
  print('Does not contain uppercase letter.')
else:
  print('Contains uppercase letter.')
  
s = 'this is Good'
if s.islower() == True:
  print('Does not contain uppercase letter.')
else:
  print('Contains uppercase letter.')
s='ch(27) + ch(97)'
print(s)
s = 'Space is a printable'
print(s)
print(s.isprintable())

s = '\nNew Line is printable'
print(s)
print(s.isprintable())

s = ''
print('\nEmpty string printable?', s.isprintable())

s = '2+2 = 4'
print(s)

if s.isprintable() == True:
  print('Printable')
else:
  print('Not Printable')
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
# example string
string = 'cat'
width = 5
# print left justified string
print(string.ljust(width))
# example string
string = 'cat'
width = 5
fillchar = '*'
# print left justified string
print(string.ljust(width, fillchar))
# example string
string = "THIS SHOULD BE LOWERCASE!"
print(string.lower())
# string with numbers
# all alphabets whould be lowercase
string = "Th!s Sh0uLd B3 L0w3rCas3!"
print(string.lower())

# first string
firstString = "PYTHON IS AWESOME!"
# second string
secondString = "PyThOn Is AwEsOmE!"
if(firstString.lower() == secondString.lower()):
    print("The strings are same.")
else:
    print("The strings are not same.")
# Leading whitepsace are removed
print(random_string.lstrip())
# Argument doesn't contain space
# No characters are removed.
print(random_string.lstrip('sti'))
print(random_string.lstrip('s ti'))
website = 'https://www.programiz.com/'
print(website.lstrip('htps:/.'))
string = "Python is fun"
# 'is' separator is found
print(string.partition('is '))
# 'not' separator is not found
print(string.partition('not '))
string = "Python is fun, isn't it"
# splits at first occurence of 'is'
print(string.partition('is'))
song = 'cold, cold heart'
print (song.replace('cold', 'hurt'))
song = 'Let it be, let it be, let it be, let it be'
'''only two occurences of 'let' is replaced'''
print(song.replace('let', "don't let", 2))
song = 'cold, cold heart'
replaced_song =  song.replace('o', 'e')
# The original string is unchanged
print ('Original string:', song)
print ('Replaced string:', replaced_song)
song = 'let it be, let it be, let it be'
# maximum of 0 substring is replaced
# returns copy of the original string
print(song.replace('let', 'so', 0))
quote= 'Let it be, let it be, let it be'
result = quote.rfind('let it')
print("Substring 'let it':", result)
result = quote.rfind('small')
print("Substring 'small ':", result)
result = quote.rfind('be,')
if  (result != -1):
  print("Highest index where 'be,' occurs:", result)
else:
  print("Doesn't contain substring")
quote = 'Do small things with great love'
# Substring is searched in 'hings with great love'
print(quote.rfind('things', 10))
# Substring is searched in ' small things with great love' 
print(quote.rfind('t', 2))
# Substring is searched in 'hings with great lov'
print(quote.rfind('o small ', 10, -1))
# Substring is searched in 'll things with'
print(quote.rfind('th', 6, 20))
quote = 'Let it be, let it be, let it be'
result = quote.rindex('let it')
print("Substring 'let it':", result)
result = quote.rindex('small')
print("Substring 'small ':", result)
quote = 'Do small things with great love'
# Substring is searched in ' small things with great love' 
print(quote.rindex('t', 2))
# Substring is searched in 'll things with'
print(quote.rindex('th', 6, 20))
# Substring is searched in 'hings with great lov'
print(quote.rindex('o small ', 10, -1))
# example string
string = 'cat'
width = 5
# print right justified string
print(string.rjust(width))
# example string
string = 'cat'
width = 5
fillchar = '*'
# print right justified string
print(string.rjust(width, fillchar))
string = "Python is fun"
# 'is' separator is found
print(string.rpartition('is '))
# 'not' separator is not found
print(string.rpartition('not '))
string = "Python is fun, isn't it"
# splits at last occurence of 'is'
print(string.rpartition('is'))
grocery = 'Milk, Chicken, Bread, Butter'
# maxsplit: 2
print(grocery.rsplit(', ', 2))
# maxsplit: 1
print(grocery.rsplit(', ', 1))
# maxsplit: 5
print(grocery.rsplit(', ', 5))
# maxsplit: 0
print(grocery.rsplit(', ', 0))
random_string = ' this is good'
# Leading whitepsace are removed
print(random_string.rstrip())
# Argument doesn't contain 'd'
# No characters are removed.
print(random_string.rstrip('si oo'))
print(random_string.rstrip('sid oo'))
website = 'www.programiz.com/'
print(website.rstrip('m/.'))





