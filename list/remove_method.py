# animal list
animal = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' element is removed
animal.remove('rabbit')

#Updated Animal List
print('Updated animal list: ', animal)


# If a list contains duplicate elements
# the remove() method removes only the first instance

# animal list
animal = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

# 'dog' element is removed
animal.remove('dog')

#Updated Animal List
print('Updated animal list: ', animal)