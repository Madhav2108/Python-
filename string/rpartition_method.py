string = "Python is fun"

# 'is' separator is found
print(string.rpartition('is '))

# 'not' separator is not found
print(string.rpartition('not '))

string = "Python is fun, isn't it"

# splits at last occurence of 'is'
print(string.rpartition('is'))