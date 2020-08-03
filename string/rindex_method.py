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