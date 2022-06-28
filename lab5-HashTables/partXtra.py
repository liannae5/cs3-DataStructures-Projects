import math
import sys

sys.setrecursionlimit(10 ** 6)  # increases recursion limit to test larger data sets


# Class that stores Passwords and their counts
class PasswordCount:
  # Constructor (Count has a default value of 0)
  def __init__(self, password, count=0):
    self.password = password
    self.count = count

  # This function is called when printing the object
  def __str__(self):
    return "Password: " + self.password + ", count: " + str(self.count)


# Method that prints all the elements in a list
def print_passwords(password_list):
  for p_count in password_list:
    print(p_count)


# A dictionary of PasswordCount objects.
# We'll talk about Dictionaries in class soon.
password_dict = {}

# Special code block to open the file.
# All the lines inside the "with" can use the file.
# After the code block is done, the file is closed automatically!
with open("10-million-combos.txt", "r", encoding="ISO-8859-1") as passwords_file:
  # This for loop iterates through each line in the text file.
  # (Yes, this is how you can write it!)
  for line in passwords_file:
    # In each line, usernames and passwords are separated with a TAB (\t)
    # If a line does not have a TAB, it does not have a UN/PWD combination
    if "\t" not in line:
      continue

    # Split the line and get the password (Position 1 after split)
    password = line.split("\t")[1].strip()

    # If we have encountered the password before, increase its count
    # otherwise, create a new PasswordCount object and add it
    if password in password_dict:
      password_obj = password_dict[password]
      password_obj.count += 1
    else:
      password_obj = PasswordCount(password, 1)
      password_dict[password] = password_obj

# Create the list for the passwords
password_list = list(password_dict.values())


#TODO: TASK 1 -- Modify this class
class SimpleMaxHeap(object):
  # Constructor
  def __init__(self):  
    self.items = []

  def is_empty(self):
    return len(self.items) == 0
  
  def parent(self,i):
    return self.items[(i-1)//2] if i > 0 else None
  
  def leftChild(self,i):
    child_idx = 2*i + 1
    if child_idx >= len(self.items):
      return None
    else: 
      return self.items[child_idx]
  
  def leftChild(self,i):
    child_idx = 2*i + 2
    if child_idx >= len(self.items):
      return None
    else: 
      return self.items[child_idx]
  
  def insert(self, item):
    # 1. Insert at end of Heap
    self.items.append(item)
    
    i = len(self.items) - 1
    # 2. As long as the element inserted is larger than its parent...
    while i > 0 and self.items[i] > self.items[(i-1)//2]:
      # 3. Swap element with its current parent
      self.items[i], self.items[(i-1)//2] = self.items[(i-1)//2], self.items[i]
      i = (i-1)//2

if __name__ == "__main__":
  #TODO: Task 2
  sortL = password_list[:10]
  print_passwords(sortL)
  heap1 = SimpleMaxHeap(sortL)
  pass #You can remove this line after completing Task 2 