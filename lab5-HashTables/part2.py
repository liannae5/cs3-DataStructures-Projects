import math
import timeit


def read_glove(filename):
  #TODO: Task 1
  words_dict = {}
  glove_vec = [] 
  with open(filename, "r", encoding="ISO-8859-1") as f:
    for line in f:
      # Simple tokenization of the line in the file
      tokens = line.replace("\n","").split(" ")
      # First token is the word
      word = tokens[0]
      if word.isalpha():
        #List comprehension for the numbers in the vector
        embedding = [float(w) for w in tokens[1:]] 
        
        words_dict[word] = embedding #uses each word as the key in the dict, and stores the embedding as its value
  return words_dict #returns word dict

def wordCompare(wdict, w1, w2):
  if w1 not in wdict or w2 not in wdict:
    print("you chose an invalid word, try again")
    return -1
  e1 = wordSearch(wdict,w1)
  e2 = wordSearch(wdict,w2)
  simResult = similarity(e1,e2)
  print(w1 + ' ' + w2 + ' ' + str(simResult))

def wordSearch(wdict, word):
  '''
  if word not in wdict:
    print(word+" is invalid")
    return -1
  '''
  return wdict[word]

def similarity(e1,e2):
  dotProd = 0  # creates variable to store dot product
  e1Mag = 0  # variable to store e1's magnitude
  e2Mag = 0  # variable to store e2's magnitude

  for i in range(len(e1)):
    dotProd += e1[i] * e2[i]  # adds each e1*e2 at each index to dot product
    e1Mag += e1[i] ** 2  # Sum of e1 vector magnitudes squares
    e2Mag += e2[i] ** 2  # Sum of e2 vector magnitudes squares

  e1Mag = math.sqrt(e1Mag)  # updates e1Mag with square root of magnitude squares
  e2Mag = math.sqrt(e2Mag)  # updates e2Mag with square root of magnitude squares
  cosineDist = dotProd / (e1Mag * e2Mag)  # calculates similarity (cosine distance)

  return cosineDist  # returns cosine distance


if __name__ == "__main__":
  #TODO: Task 2
  print("total time adding all elements to dict: "+str(timeit.timeit(stmt=lambda: read_glove("glove.6B.50d.txt"), number=1)))
  wordDict = read_glove("glove.6B.50d.txt")

  #uncomment for runtime tests

  print("Runtimes for dict to find each word in wordSearch method tests")
  print("Search time for sneakers: " + str(timeit.timeit(stmt=lambda: wordSearch(wordDict, "sneakers"), number=1)))
  print("Search time for sitar: " + str(timeit.timeit(stmt=lambda: wordSearch(wordDict, "sitar"), number=1)))
  print("Search time for pen: " + str(timeit.timeit(stmt=lambda: wordSearch(wordDict, "pen"), number=1)))
  print("Search time for paper: " + str(timeit.timeit(stmt=lambda: wordSearch(wordDict, "paper"), number=1)))
  print("Search time for faith: " + str(timeit.timeit(stmt=lambda: wordSearch(wordDict, "faith"), number=1)))
  print("Search time for hope: " + str(timeit.timeit(stmt=lambda: wordSearch(wordDict, "hope"), number=1)))
  print("Search time for harvard: " + str(timeit.timeit(stmt=lambda: wordSearch(wordDict, "faith"), number=1)))
  print("Search time for stanford: " + str(timeit.timeit(stmt=lambda: wordSearch(wordDict, "stanford"), number=1)))


  # uncomment to test wordCompare

  print("Test1: ")
  word1 = input("Input first word: ")
  word2 = input("Input second word: ")
  wordCompare(wordDict, word1, word2)
  '''
  print("Test2: ")
  word1 = input("Input first word: ")
  word2 = input("Input second word: ")
  wordCompare(wordDict, word1, word2)
  print("Test3: ")
  word1 = input("Input first word: ")
  word2 = input("Input second word: ")
  wordCompare(wordDict, word1, word2)
  print("Test4: ")
  word1 = input("Input first word: ")
  word2 = input("Input second word: ")
  wordCompare(wordDict, word1, word2)
  print("Test5: ")
  word1 = input("Input first word: ")
  word2 = input("Input second word: ")
  wordCompare(wordDict, word1, word2)
'''