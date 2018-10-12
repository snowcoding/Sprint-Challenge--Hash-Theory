import re
# Find regexes that match the following. (e.g. find a single regex that matches
# both `antelope` and `antelopes`.)
line1 = 'antelope'
line2 = 'antelopes'
line3 = 'antelop'

print("\nRegex 1:")
match1 = re.match('antelopes?', line1)
match2 = re.match('antelopes?', line2)
match3 = re.match('antelopes?', line3)
print (f"testing {line1}: {match1.group()}" )
print (f"testing {line2}: {match2.group()}" )
print (f"testing {line3}: {match3}" )

# * Single regex that matches either of these:

#     antelope rocks out
    
#     antelopes rock out

line1 = 'antelope rocks out'
line2 = 'antelopes rock out'
line3 = 'antelopes rock '

print("\nRegex 2:")
match1 = re.match('antelopes? rocks? out', line1)
match2 = re.match('antelopes? rocks? out', line2)
match3 = re.match('antelopes? rocks? out', line3)
print (f"testing {line1}: {match1.group()}" )
print (f"testing {line2}: {match2.group()}" )
print (f"testing {line3}: {match3}" )

# * Regex that matches either of:

#     goat
    
#     moat

#   but not:

#     boat

line1 = 'goat'
line2 = 'moat'
line3 = 'boat'

print("\nRegex 3:")
match1 = re.match('[gm]oat', line1)
match2 = re.match('[gm]oat', line2)
match3 = re.match('[gm]oat', line3)
print (f"testing {line1}: {match1.group()}" )
print (f"testing {line2}: {match2.group()}" )
print (f"testing {line3}: {match3}" )

# * Regex that matches dates in YYYY-MM-DD format. (Year can be 1-4 digits, and
#   month and day can each be 1-2 digits). This does not need to verify the date
#   is correct (e.g 3333-33-33 can match).

#   2000-10-12
  
#   1999-1-20
  
#   1999-01-20
  
#   812-2-10

line1 = '2000-10-12'
line2 = '1999-1-20'
line3 = '1999-01-20'
line4 = '812-2-10'
line5 = '2ooo-10-12'

print("\nRegex 4:")
match1 = re.match('[0-9]{1,4}-[0-9]{1,2}-[0-9]{1,2}', line1)
match2 = re.match('[0-9]{1,4}-[0-9]{1,2}-[0-9]{1,2}', line2)
match3 = re.match('[0-9]{1,4}-[0-9]{1,2}-[0-9]{1,2}', line3)
match4 = re.match('[0-9]{1,4}-[0-9]{1,2}-[0-9]{1,2}', line4)
match5 = re.match('[0-9]{1,4}-[0-9]{1,2}-[0-9]{1,2}', line5)
print (f"testing {line1}: {match1.group()}" )
print (f"testing {line2}: {match2.group()}" )
print (f"testing {line3}: {match3.group()}" )
print (f"testing {line4}: {match4.group()}" )
print (f"testing {line5}: {match5}" )

