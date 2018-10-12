def get_indices_of_item_weights(weights, limit):
  # Init the hash table
  ht = {}
  
  # if len = 1 return empty tuple
  if len(weights) == 1:
    return ()
  
  # if len = 2 return tuple with 1,0
  if len(weights) ==2:
    if (weights[0] + weights[1] == limit):
      return (1,0)

  # Set the keys in ht as the weights and values as index
  for i, w in enumerate(weights):
    ht[w] = i

  for key in ht:
    try:
      # See if the difference exits
      keyTest = ht[limit-key]
      if (keyTest):
        # if it does return the tuple of indexes
        return (ht[limit-key], ht[key])
    except KeyError: 
      print('Missed key... move to next key')
      

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  print("\ntest 1")
  print(get_indices_of_item_weights([9], 9))
  print("\ntest 2")
  print(get_indices_of_item_weights([4, 4], 8))
  print("\ntest 3")
  print(get_indices_of_item_weights([4, 6, 10, 15, 16], 21))
  print("\ntest 4")
  print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 7))
  

  