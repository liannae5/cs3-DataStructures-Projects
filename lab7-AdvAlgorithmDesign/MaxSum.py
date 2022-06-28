
'''
CS 2302
Lab 7
MaxSum.py

Student Name: Lianna Estrada
Student ID: 80642079
Last Modified: 05/08/2022
'''
class Node:
  def __init__(self, left=None, right=None, item=None):
    self.left = left
    self.right = right
    self.item = item

def max_sum(root):
  #returns root if root is the only node in the tree
  if root.left == None and root.right == None:
    return root.item
  visitedQ = [] #queue to store nodes to visit
  sumList = [[root.item]] #stores list of sums
  visitedQ.append(root) #adds root to queue
  levelCount = 1 #level of root is 1
  while len(visitedQ) != 0: #while queue isn't empty
    levelSums = [] #reset list of all possible sums for given level
    i = 0 #set index
    while i < 2**(levelCount-1): #checks each node on a level
      if len(visitedQ) != 0: #ensures queue isn't empty
        currN = visitedQ.pop(0) #if queue isn't empty update current node by dequeueing from visitedQ
      if currN.left is not None: #if currN has a left child
        visitedQ.append(currN.left) #enqueue node
        #uncomment to do runtime testslevelSums.append(2+ 0)
        levelSums.append(sumList[levelCount-1][i]+currN.left.item) #append level-1 sum+left child's value to levelSums (comment out for runtime tests)
      if currN.right is not None:#if currN has right child
        visitedQ.append(currN.right) #enqueue right child
        #uncomment to run runtime tests. levelSums.append(2 + 0)
        levelSums.append(sumList[levelCount-1][i] + currN.right.item) #append level-1 sum+right child's value to levelSums (comment out for runtime tests)
      i +=1 #increase i
    if len(levelSums) != 0: #adds all but last levelSum list to sumList
      sumList.append(levelSums)
    levelCount +=1 #increases level count


  #checks if tree is not perfect. If it's not perfect then None is returned

  if len(sumList[-1]) < 2**(levelCount-2):
    print("Tree is invalid because it is not a perfect tree")
    return None

  # last list in sumList holds the total sum for each possible path
  maxVal = sumList[-1][0]  # set first val in last levelSum list as maxVal
  #check last list and update maxVal if a greater sum is found
  for value in sumList[-1]:
    if value > maxVal:
      maxVal = value
  return maxVal #returns maxVal



'''the following functions are used for testing in main.py'''
#USED IN TEST 2.tree with 3 levels, each level has nodes where each has a greater value than any node in previous level
def generate_example_tree2():


  c1 = Node(item=32)
  c2 = Node(item=50)
  c3 = Node(item=40)

  b1 = Node(left=c1, right=c2, item=21)
  b2 = Node(left=c2, right=c3, item=20)

  root = Node(left=b1, right=b2, item=5)

  return root

#USED IN TEST 3. tree with 4 level, is imperfect
def generate_example_tree3():

  e1 =Node(item=0)
  e2 = Node(item=-300)
  e3= Node(item=-77)
  e4= Node(item=-68)


  d1 = Node(left=e1,right=e2,item=1)
  d2 = Node(left=e2,right=e3 ,item=63)
  d3 = Node(left=e3,right=e4 ,item=-43)
  d4 = Node(left=e4,right=None,item=-5)

  c1 = Node(left=d1,right=d2 ,item=-98)
  c2 = Node(left=d2,right=d3 ,item=11)
  c3 = Node(left=d3,right=d4 ,item=200)

  b1 = Node(left=c1, right=c2, item=31)
  b2 = Node(left=c2, right=c3, item=-13)

  root = Node(left=b1, right=b2, item=-1)

  return root

#USED IN TEST 4. tree with 8 levels, all nodes have a negative value
def generate_example_tree4():

  h1=Node(item=-420)
  h2=Node(item=-964)
  h3=Node(item=-43)
  h4=Node(item=-6)
  h5=Node(item=-7)
  h6=Node(item=-2014)
  h7=Node(item=-32)
  h8=Node(item=-97)

  g1=Node(left=h1,right=h2,item=-6382)
  g2=Node(left=h2,right=h3,item=-862)
  g3=Node(left=h3,right=h4,item=-553)
  g4=Node(left=h4,right=h5,item=-372)
  g5=Node(left=h5,right=h6,item=-46)
  g6=Node(left=h6,right=h7,item=-1)
  g7=Node(left=h7,right=h8,item=-4)


  f1=Node(left=g1,right=g2,item=-85)
  f2=Node(left=g2,right=g3,item=-91032)
  f3=Node(left=g3,right=g4,item=-77)
  f4=Node(left=g4,right=g5,item=-23)
  f5=Node(left=g5,right=g6,item=-47)
  f6=Node(left=g6,right=g7,item=-1100)

  e1 = Node(left=f1,right=f2,item=-90)
  e2 = Node(left=f2,right=f3,item=-300)
  e3 = Node(left=f3,right=f4,item=-77)
  e4 = Node(left=f4,right=f5,item=-68)
  e5 = Node(left=f5,right=f6,item=-990)

  d1 = Node(left=e1, right=e2, item=-1)
  d2 = Node(left=e2, right=e3, item=-63)
  d3 = Node(left=e3, right=e4, item=-43)
  d4 = Node(left=e4, right=e5, item=-5)

  c1 = Node(left=d1, right=d2, item=-98)
  c2 = Node(left=d2, right=d3, item=-11)
  c3 = Node(left=d3, right=d4, item=-200)

  b1 = Node(left=c1, right=c2, item=-31)
  b2 = Node(left=c2, right=c3, item=-13)

  root = Node(left=b1, right=b2, item=-8)

  return root
