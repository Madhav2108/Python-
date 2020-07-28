sentence = 'Python programming is fun.'

# Substring is searched in 'gramming is fun.'
print(sentence.index('ing', 10))

# Substring is searched in 'gramming is '
print(sentence.index('g is', 10, -4))

# Substring is searched in 'programming'
print(sentence.index('fun', 7, 18))