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
print(song.replace('let', 'so', 0)