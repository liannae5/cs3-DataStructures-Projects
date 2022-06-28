'''
CS 2302
Lab 4: Trees
part1.py

Student Name: Lianna Estrada
Student ID: 80642079
Last Modified: 3/13/2022
'''
import math
import timeit
from glove_reader import read_glove
import sys
# Sample code to show how to read the embeddings
print("total time adding all elements to dict: "+str(timeit.timeit(stmt=lambda: read_glove("glove.6B.50d.txt"), number=1)))
(words_lst, embeddings_lst) = read_glove("glove.6B.50d.txt")
wordsT = (words_lst, embeddings_lst)


#TODO: Task 1 code
#The following AVL Tree implementation is from this website: https://www.programiz.com/dsa/avl-tree

#Defines TreeNode class to be used in AVL Tree class
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

#defines AVLTree class
class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, key):
        # Find the correct location and insert the node
        #if node is null, returns a node with key
        if not root:
            return TreeNode(key)
        #recursively looks for position in root's left subtree if key word < root's word
        elif key["word"] < root.key["word"]:
            root.left = self.insert_node(root.left, key)
        #otherwise recursively looks for position in root's right subtree
        else:
            root.right = self.insert_node(root.right, key)

        #updates root's height
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree

        #gets balance factor of root
        balanceFactor = self.getBalance(root)

        # rotates root's left node right if balance factor >1
        if balanceFactor > 1:
            if key["word"] < root.left.key["word"]:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        # rotates root's right node left if balance factor <-1
        if balanceFactor < -1:
            if key["word"] > root.right.key["word"]:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root #returns root of tree updated with the insertion

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it

        #if root is null, returns null
        if not root:
            return root

        #recursively calls the function on root's left node if the key word is less than root's word
        elif key["word"] < root.key["word"]:
            root.left = self.delete_node(root.left, key)

        # recursively calls the function on root's right node if the key word is more than root's word
        elif key["word"] > root.key["word"]:
            root.right = self.delete_node(root.right, key)
        #if the key word matches the root's word, it is removed
        else:
            #if left or right child node is null, deletes root and returns the opposite child node
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            #otherwise recursively calls on min value of root's right subtree
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        #if root is null returns root
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        #finds balance factor
        balanceFactor = self.getBalance(root)

        # Balance the tree
        #rotates root's left node right if balance factor >1
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        # rotates root's right node left if balance factor <-1
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root #returns the root of the tree updated with the deletion

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right #holds z's right node
        T2 = y.left #holds y's left node
        #swap
        y.left = z #updates y's new left node as z
        z.right = T2 #updates z's new right node as y's initial left node

        #updates z and y's height
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left #holds z's left node
        T3 = y.right #hold's y's right node
        #swap
        y.right = z #updates y's new right node as z
        z.left = T3 #updates z's new left as y's initial right node

        #updates z and y's heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        # Returns zero if node is null
        if not root:
            return 0
        #Returns node's height attribute value
        return root.height

    # Get balance factor of the node
    def getBalance(self, root):
        #Returns zero if node is null
        if not root:
            return 0
        #Returns the difference between the height of 2 nodes to determine balance factor
        return self.getHeight(root.left) - self.getHeight(root.right)

    #Returns minimum value in the tree
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)


    #Prints tree values in preOrder
    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key["word"]), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    # Prints a visual representation of the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key["word"])
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)



#TODO: Task 2 code
def addWords(words):
    wordsAVL = AVLTree() #Creates empty AVL Tree
    wroot = None #Creates empty root
    #print("words length: "+str(len(words[0])))
    for ind in range(len(words[0])): #iterates through each word in the list
        #creates an individual dict for each word and its respective embedding
        dictVal = {
            "word": words[0][ind], #stores the word at ind as key of dict
            "embed": words[1][ind]
        }
        wroot = wordsAVL.insert_node(wroot, dictVal) #inserts the dict into the AVL Tree

    return (wordsAVL,wroot) #Returns a tuple containing the AVL Tree and its root node

#Creates AVL Tree
avl = addWords(wordsT) #creates the AVL Tree out of the words list
avlTree = avl[0] #Stores the tree
avlRoot = avl[1] #Stores the root
#print("Tree height: "+str(avlTree.getHeight(avlRoot)))

#TODO: Task 3 code

#method compares two word's embeddings and prints their similarity
def wordCompare(root,word1, word2):
    w1Embed = avlSearch(root,word1) #searches for word1 and stores its embedding
    w2Embed = avlSearch(root, word2) #searches for word2 and stores its information
    simResult = similarity(w1Embed,w2Embed) #stores the similarity between the two words
    print(word1+ ' '+word2 +' '+str(simResult)) #prints the result

#Recursive method to search for a word in the AVL Tree
def avlSearch(root, word):

    #Returns null if the word isn't found
    if(root.key == None):
        print("word not found")
        return

    #Returns word's corresponding embed if word equals root's word
    if(word == root.key["word"]):
        return root.key["embed"]

    #Makes recursive call on root's left subtree if the word < root's word
    if(word < root.key["word"]):
        return avlSearch(root.left, word)

    #otherwise makes recursive call on root's right subtree if the word > root's word
    return avlSearch(root.right, word)

#Method calculates similarity between two words
def similarity(e1, e2):
    dotProd = 0 #creates variable to store dot product
    e1Mag = 0 #variable to store e1's magnitude
    e2Mag = 0 #variable to store e2's magnitude

    for i in range(len(e1)):
        dotProd += e1[i]*e2[i] #adds each e1*e2 at each index to dot product
        e1Mag += e1[i]**2 #Sum of e1 vector magnitudes squares
        e2Mag += e2[i]**2 #Sum of e2 vector magnitudes squares

    e1Mag = math.sqrt(e1Mag) #updates e1Mag with square root of magnitude squares
    e2Mag = math.sqrt(e2Mag) #updates e2Mag with square root of magnitude squares
    cosineDist = dotProd/(e1Mag*e2Mag) #calculates similarity (cosine distance)

    return cosineDist #returns cosine distance

#uncomment to test runtimes for AVLSearch

print("Runtimes for using AVL Search to find each word in AVLSearch method tests")
print("Search time for sneakers: "+str(timeit.timeit(stmt=lambda: avlSearch(avlRoot,"sneakers"), number=1)))
print("Search time for sitar: "+str(timeit.timeit(stmt=lambda: avlSearch(avlRoot,"sitar"), number=1)))
print("Search time for pen: "+str(timeit.timeit(stmt=lambda: avlSearch(avlRoot,"pen"), number=1)))
print("Search time for paper: "+str(timeit.timeit(stmt=lambda: avlSearch(avlRoot,"paper"), number=1)))
print("Search time for faith: "+str(timeit.timeit(stmt=lambda: avlSearch(avlRoot,"faith"), number=1)))
print("Search time for hope: "+str(timeit.timeit(stmt=lambda: avlSearch(avlRoot,"hope"), number=1)))
print("Search time for harvard: "+str(timeit.timeit(stmt=lambda: avlSearch(avlRoot,"faith"), number=1)))
print("Search time for stanford: "+str(timeit.timeit(stmt=lambda: avlSearch(avlRoot,"stanford"), number=1)))



#uncomment to test wordCompare
'''
print("Test1: ")
word1 = input("Input first word: ")
word2 = input("Input second word: ")
wordCompare(avlRoot, word1, word2)
print("Test2: ")
word1 = input("Input first word: ")
word2 = input("Input second word: ")
wordCompare(avlRoot, word1, word2)

print("Test3: ")
word1 = input("Input first word: ")
word2 = input("Input second word: ")
wordCompare(avlRoot, word1, word2)
print("Test4: ")
word1 = input("Input first word: ")
word2 = input("Input second word: ")
wordCompare(avlRoot, word1, word2)
print("Test5: ")
word1 = input("Input first word: ")
word2 = input("Input second word: ")
wordCompare(avlRoot, word1, word2)
'''