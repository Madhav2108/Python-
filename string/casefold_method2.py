firstString = "der Fluß"
secondString = "der Flusss"

# ß is equivalent to ss
if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')