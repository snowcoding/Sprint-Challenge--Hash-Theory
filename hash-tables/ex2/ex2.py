def reconstruct_trip(tickets):
  # Initialize the hash table
  ht = {}

  # Initialize final route
  route = []

  # Loop through the ticket list and populate the keys as
  # the start and then values as the destinations
  for t in tickets:
    print(t)
    ht[t[0]] = t[1]

  # Test for membership via try/except block  
  try:
    # Set the current pointer to the index where None is the key
    current = ht[None]

    # Set the first entry of route to be that current
    route.append(current)

    # Set next to also be the same as current
    next = ht[None] 

    # Keep looping while the next is not None
    while (next != None):
      try:
        # Update the pointer
        next = ht[next]
        
        if (next):
          route.append(next)
      except:
        return []
    
    return route

  except:
    return []

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  short_set = [
      (None, 'PDX'),
      ('PDX', 'DCA'),
      ('DCA', None)
    ]
  print('\ntest 1')
  print(reconstruct_trip(short_set))

  long_set = [
    ('PIT', 'ORD'),
    ('XNA', 'CID'),
    ('SFO', 'BHM'),
    ('FLG', 'XNA'),
    (None, 'LAX'), 
    ('LAX', 'SFO'),
    ('CID', 'SLC'),
    ('ORD', None),
    ('SLC', 'PIT'),
    ('BHM', 'FLG'),
  ]
  print('\ntest 2')
  print(reconstruct_trip(long_set))
