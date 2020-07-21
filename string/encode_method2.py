# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# ignore error
print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))

# replace error
print('The encoded version (with replace) is:', string.encode("ascii", "replace"))