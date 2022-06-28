'''
CS 2302
Lab 4: Trees
part2.py

Student Name: Lianna Estrada
Student ID: 80642079
Last Modified: 3/18/2022
'''
from venv import create
from tree import TreeNode,  rootOnlyTree, rightNodesOnly, negativeNumMix, nSizeTree, preOrderPrint
import timeit
import sys
sys.setrecursionlimit(10**6) #increases recursion limit to test larger data sets
# Method that computes the average of levels in the tree
def average_of_levels(root):

  #Returns empty list if tree is empty
  if root == None:
    print("Tree is empty!")
    return []

  treeHeight = getHeight(root) #gets tree height
  avgList = [] #initializes list to store level averages

  #Finds average of each level in the tree
  for level in range(treeHeight+1):
    tempList = findAvgValues(root,level)  #stores tuple containing level's total sum and number of nodes
    avgList +=[tempList[0]/tempList[1]] #adds the average of the current level to corresponding list index in avgList

  return avgList #returns list of level averages


#Recursively finds total sum of all nodes in the level and tally of number of nodes in the level
def findAvgValues(root, level):
  levelSum = 0 #initializes variable to keep track of total sum
  totalNodes = 0 #initializes variable to keep track of number of nodes in the level

  #Returns tuple of zeroes if root is null
  if root == None:
    return (0, 0)

  #Returns tuple containing root's value and a tally of 1 node if at level 0
  if level == 0:
    return (root.item, 1)

  #if root's left child isn't null makes recursive call on root's left subtree and decreases level
  if root.left != None:
    tempList = findAvgValues(root.left, level - 1)
    levelSum += tempList[0] #adds sum of left side values to levelSum total
    totalNodes += tempList[1] #stores tally of left side's nodes
  # if root's right child isn't null makes recursive call on root's right's subtree and decreases level
  if root.right != None:
    tempList = findAvgValues(root.right, level - 1)
    levelSum += tempList[0] #adds sum of right side values to levelSum total
    totalNodes += tempList[1] #stores tally of right side's nodes

  # Returns tuple with first value being the total sum of the level, the second being the node tally
  return (levelSum, totalNodes)

#Method to get tree's height
def getHeight(root):
  #if root is null return -1
  if root == None:
     return -1
  #recursive call on root's right subtree to find right height
  rightHeight = getHeight(root.right)
  # recursive call on root's right subtree to find right height
  leftHeight = getHeight(root.left)

  #Sets whichever side's heightis greater to the height of the entire tree and returns it
  if rightHeight >= leftHeight:
    return rightHeight+1
  return leftHeight+1

# Test case code
root1 = negativeNumMix()
root2 = rootOnlyTree()
root3 = rightNodesOnly()
assert average_of_levels(root1) == [-6.0, 22.0, 20.4175, -29.0, 0.0], "Test 1: FAILED"
assert average_of_levels(root2) == [42.0], "Test 2: FAILED"
assert average_of_levels(root3) == [22.0, -5.0, 11.0, 32.0, -57.0, 96.0, 2.0], "Test 3: FAILED"

#Uncomment below to print test results to the screen
'''
print("test1 preorder: -6, 77, 99, 29, 47, 16, -33, 2.67, -4, -103,-11.6, 11.6")
print("Expected: "+str([-6.0, 22.0, 20.4175, -29.0, 0.0]))
print("Actual: "+str(average_of_levels(root1)))
print("test2 preorder: 42")
print("Expected: "+str([42.0]))
print("Actual: "+str(average_of_levels(root2)))
print("test3 preorder: 22, -5, 11, 32, -57, 96, 2.0")
print("Expected "+str([22.0, -5.0, 11.0, 32.0, -57.0, 96.0, 2.0]))
print("Actual: "+str(average_of_levels(root3)))
'''

#Uncomment for runtime tests
'''
rtSizeList = [10,100,500,1000,1500,2000,3000,4000,5000] #Tree sizes
for i in rtSizeList:
  root = nSizeTree(i)
  print("Runtime for tree with "+ str(i) + " nodes: "+ str(timeit.timeit(stmt=lambda: average_of_levels(root), number=1)))
  print("averages"+str(average_of_levels(root)))
'''