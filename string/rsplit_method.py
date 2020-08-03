grocery = 'Milk, Chicken, Bread, Butter'

# maxsplit: 2
print(grocery.rsplit(', ', 2))

# maxsplit: 1
print(grocery.rsplit(', ', 1))

# maxsplit: 5
print(grocery.rsplit(', ', 5))

# maxsplit: 0
print(grocery.rsplit(', ', 0))