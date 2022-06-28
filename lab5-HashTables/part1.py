
import random
import timeit
import string
class doubleLLNode:
  def __init__(self, key, value):
    self.key = key #to hold the key
    self.value = value #to hold the value
    self.previous = None #node's previous pointer
    self.next = None #node's next pointer

class LRUCache:
  def __init__(self, max_cap=6000):
    self.max_cap = max_cap # maximum memory capacity
    self.length = 0 # total of items in LRU
    self.cache = {} #creates dict for values
    self.lastDeleted = [None,None] #holds the key and value of deleted key previously in cache
    self.head = doubleLLNode(None,None) #lru's head in doubly linked list (least recent item)
    self.tail = doubleLLNode(None,None) #lru's tail in doubly linked list (most recent item)
    self.cHead = None #holds key of cache head
    self.cTail = None #holds key of cache tail

  # TODO: Implement this method - Required Time Complexity: O(1)
  #Gets value of key if in cache, otherwise returns None
  def get(self, key):
    if key not in self.cache:
      print("Key not found!")
      return None # returns none if key is not in the cache dict
    else:
      return self.cache[key] #returns key's associated value otherwise
      
  # TODO: Implement this method - Required Time Complexity: O(1)
  #inserts a key and node into the cache
  def put(self, key, value):
    newNode = doubleLLNode(key, value) #makes a node out of the new key and value
    #what occurs when the key exists in the cache
    if key in self.cache:

      #when the head matches the key
      if key == self.head.key:
        self.replaceHead() #updates head
        self.cache[key] = value  # adds key and value to cache
        oldTail = self.tail #holds current
        self.tail.next = newNode #sets current tail's next pointer to newNode
        self.tail = self.tail.next #updates tail
        self.tail.previous = oldTail #sets new tail's previous pointer to the oldTail
        self.cTail = self.tail.key


      else:
        self.lastDeleted = [key, self.cache[key]] #holds last deleted value
        del self.cache[key] #deletes old value matched with key
        self.cache[key] = value #updates cache with key
        #when the key matches the tail key
        if key == self.tail.key:
          oldTail =self.tail #holds current tail
          tailPrev = self.tail.previous #holds tail's previous node
          tailPrev.next = newNode #sets tail's prev node to new Node
          self.tail = tailPrev.next #updates tail
          self.tail.previous = tailPrev #updates tail's previous pointer to tailPrev node

        else:
          self.replaceTail(newNode) #replaces tail accordingly

    #when the cache has not reached max cap. key does not exit in cache
    elif self.length < self.max_cap:
      self.cache[key] = value #adds new key and value to cache dict
      self.length += 1 #increases cache size

      #when cache is empty
      if self.head.key is None:
        headNode = newNode
        #head and tail node/key are the same
        self.head = headNode
        self.tail = headNode
        self.cHead = key
        self.cTail = key
      #when there's only one item in cache
      elif self.head == self.tail:
        self.head.next = newNode #head's next pointer point to newNode
        self.tail = self.head.next #tail = node after head
        self.cTail = self.tail.key #cTail = link's tail key
        self.tail.previous = self.head #cHead = link's head key

      #otherwise, we just need to replace tail with newNode
      else:
       self.replaceTail(newNode)

    #when cache is full
    else:
      self.cache[key] = value #update cache with new key and value
      self.replaceHead() #get rid of least recently used item
      self.replaceTail(newNode) #update tail with new key and value


  #updates head
  def replaceHead(self):
    oldHead = self.head  # holds oldHead (lecent recently used item)
    self.head = self.head.next  # updates head to head.next
    self.cHead = self.head.key #updates cache head key
    self.head.previous = None  # set's new head's next pointer to None
    del self.cache[oldHead.key]  # delete's oldHead from the cache dict
    del oldHead  # deletes the oldHead node

  #upates tail
  def replaceTail(self, newNode):
    self.tail.next = newNode #sets newNode to the current tail's pointer
    oldTail = self.tail #holds old tail node
    self.tail = self.tail.next #updates tail to new node
    self.cTail = self.tail.key #updates cache tail key
    self.tail.previous = oldTail #sets oldTail to updated tail's new previous pointer


  # TODO: Implement this method - Required Time Complexity: O(1)
  # Returns the number of key/value pairs currently stored in the cache
  def size(self):
    return self.length #returns length of
  
  # TODO: Implement this method - Required Time Complexity: O(1)
  # Returns the maximum capacity of the cache
  def max_capacity(self):
    return self.max_cap #returns the value at max_capacity


  # TODO: Implement this method - Required Time Complexity: O(1)
  # Returns the least-recently used item in the cache
  def peek(self):
    return "(\""+str(self.cHead)+"\", "+str(self.cache[self.cHead])+")" #returns key value equivalent to head key

  # TODO: Implement this method - Required Time Complexity: O(n)
  def toString(self):
    temp = self.head #holds lru's head so the doubly-linked list can be iterated through
    lstLen = self.size() #holds cache's length
    str_cache = [None] * lstLen #creates empty list to hold values
    for i in range(lstLen): #iterates through each key
      str_cache[i] = "(\""+str(temp.key)+"\", "+str(self.cache[temp.key])+")" #adds each key and value to list
      temp = temp.next #updates temp to next node in list
    return str(str_cache) #returns list of keys and their values in order of least recent to most recent


  # Other methods -- you do not need to change these
  def __getitem__(self, key):
    return self.get(key)
  
  def __setitem__(self, key, item):
    self.put(key, item)
  
  def __len__(self):
    return self.size()
  
  def __str__(self):
    return self.toString()

if __name__ == "__main__":

  #TEST CODE
  #uncomment to run test code
  """
  cache1 = LRUCache(10)
  cache2 = LRUCache(8)
  cache3 = LRUCache(6)


  keys1 = ['Murray','Poeltl','Johnson','Primo','Walker','Richardson','Collins', 'Jones']
  keys2 = ['Murray', 'Poeltl', 'Johnson', 'Primo', 'Walker', 'Richardson', 'Collins', 'Murray']
  keys3 =  ['Murray','Poeltl','Johnson','Primo','Walker','Richardson','Collins', 'Jones',
            'Vassell','Primo','Landale']

  vals = [5,25,3,11,1,7,23,33,35,24,17,34,15,31,28,18,42,99]

  for k,v in zip(keys1, vals):
    cache1[k] = v # Calls __setitem__
  cache_str1 = str(cache1) # Calls __str__
  for k,v in zip(keys2, vals):
    cache2[k] = v # Calls __setitem__
  cache_str2 = str(cache2) # Calls __str__
  for k,v in zip(keys3, vals):
    cache3[k] = v # Calls __setitem__
  cache_str3 = str(cache3) # Calls __str__
  print("cache1")
  print('Keys: '+str(keys1))
  print('Values: '+str(vals))
  print("Created cache: Least-recently used --> Most-recently used")
  print(cache_str1)
  print("Max capacity: "+str(cache1.max_capacity()))
  print("Size, expected is 8, actual is: " + str(cache1.size()))
  print("getting value for key 'Landale':")
  print(str(cache1.get('Landale')))
  print("Peek. Expected is ('Murray', 5). Actual is: "+str(cache1.peek()))
  print("putting ('Mills', 8)")
  print("Updated Cache:")
  cache1.put("Mills",8)
  cache_str1=str(cache1)
  print(cache_str1)

  print("cache2")
  print('Keys: ' + str(keys2))
  print('Values: ' + str(vals))
  print("Created cache: Least-recently used --> Most-recently used")
  print(cache_str2)
  print("Max capacity: " + str(cache2.max_capacity()))
  print("Size, expected is 7, actual is: " + str(cache2.size()))
  print("getting value for key 'Murray':")
  print(str(cache2.get('Murray')))
  print("Peek. Expected is ('Poeltl', 25). Actual is: " + str(cache2.peek()))
  print("putting ('Mills', 8)")
  print("Updated Cache:")
  cache2.put("Mills", 8)
  cache_str2 = str(cache2)
  print(cache_str2)

  print("cache3")
  print('Keys: ' + str(keys3))
  print('Values: ' + str(vals))
  print("Created cache: Least-recently used --> Most-recently used")
  print(cache_str3)
  print("Max capacity: " + str(cache3.max_capacity()))
  print("Size, expected is 6, actual is: " + str(cache3.size()))
  print("getting value for key 'Primo':")
  print(str(cache3.get('Primo')))
  print("Peek. Expected is ('Richardson', 7). Actual is: " + str(cache3.peek()))
  print("putting ('Mills', 8)")
  print("Updated Cache:")
  cache3.put("Mills", 8)
  cache_str3 = str(cache3)
  print(cache_str3)
  """
  #RUNTIME CODE
  #uncomment to run runtime code
  '''
  cacheSize = [10,50, 100, 500, 1000,2000,5000]
  searchKey = None
  cache = None
  for i in cacheSize:
    print("CACHE SIZE: "+str(i))
    for j in range(i):
      cache = None
      cache = LRUCache(i)
      if j == i//2:
        key = random.choice(string.ascii_uppercase)
        searchKey = key
        val = random.randint(3,1500)
        print("Put() time for "+key+", "+str(val) +": "+ str(timeit.timeit(stmt=lambda: cache.put(key,val), number=1)))
      else:
        key = random.choice(string.ascii_uppercase)
        val = random.randint(3, 1500)
        cache[key] = val
    print("Get() time for " + searchKey +": " + str(timeit.timeit(stmt=lambda: cache.get(searchKey), number=1)))
    print("Peek() time: "+str(timeit.timeit(stmt=lambda: cache.peek(), number=1)))
    print("Size() time: " + str(timeit.timeit(stmt=lambda: cache.size(), number=1)))
    print("Max_cap() time: " + str(timeit.timeit(stmt=lambda: cache.max_capacity(), number=1)))
    print("toString() time: "+ str(timeit.timeit(stmt=lambda: cache.toString(), number=1)))
    '''



