'''
CS 2302
Lab 7
main.py

Student Name: Lianna Estrada
Student ID: 80642079
Last Modified: 05/08/2022
'''
import MaxSum
import StudyGuide
import timeit

if __name__ == "__main__":
  print("Sample Problems")
  print("=" * 10)
  #uncomment below to run test cases for part 1
  '''
  print("Part 1: Study Guides")
  print("TEST CASES")
  print("~~~TEST 1~~~~")
  #tests that program generally works when times and weights only increase
  study1=[(10,20),(22,32),(40,50),(45,60)]
  mt1 = 62
  type1_result1 = StudyGuide.getBestGuide_type1(study1, mt1)
  type2_result1 = StudyGuide.getBestGuide_type2(study1, mt1)
  print("list: "+str(study1))
  print("type 1 expected: ([0, 1, 1, 0], 62, 82)")
  print(f"Actual Type 1: {type1_result1}")
  print("type 2 expected: ([1, 1, 0, 0.6666666666666666], 62, 92.0)")
  print(f" Actual Type 2: {str(type2_result1)}")

  print("~~~TEST 2~~~~")
  #tests that the program works when the maxTime is less than all other of the chapter study times in the list
  study2=[(10,20),(22,32),(40,50),(45,60),(75,88),(82,99)]
  mt2 = 5
  type1_result2 = StudyGuide.getBestGuide_type1(study2, mt2)
  type2_result2 = StudyGuide.getBestGuide_type2(study2, mt2)
  print("list: "+str(study2))
  print("type 1 expected: ([0, 0, 0, 0, 0, 0], 0, 0)")
  print(f" Actual Type 1: {type1_result2}")
  print("type 2 expected: ([0, 0, 0, 0, 0], 0, 0)")
  print(f" Actual Type 2: {str(type2_result2)}")

  print("~~~TEST 3~~~~")
  #
  study3 = [(22, 32), (40, 50), (75, 88),(45, 60), (10, 20),(5,1),(47,20),(33,43),(100,200)]
  mt3 = 89
  type1_result3 = StudyGuide.getBestGuide_type1(study3, mt3)
  type2_result3 = StudyGuide.getBestGuide_type2(study3, mt3)
  print("list: "+str(study3))
  print("type 1 expected: ([0, 0, 0, 1, 1, 0, 0, 1, 0], 88, 123)")
  print(f" Actual Type 1: {type1_result3}")
  print("type 2 expected: ([0, 0, 0, 0, 0, 0, 0, 0, 0.89], 89, 178.0)")
  print(f" Actual Type 2: {str(type2_result3)}")

  print("~~~TEST 4~~~~")
  #tests to see if program works when all chapters have the same
  study4 = [(15,20),(15,20),(15,20),(15,20),(15,20),(15,20),(15,20),(15,20),(15,20),(15,20),(15,20),(15,20),(15,20),(15,20),(15,20),(15,20),(15,20)]
  mt4 = 43
  type1_result4 = StudyGuide.getBestGuide_type1(study4, mt4)
  type2_result4 = StudyGuide.getBestGuide_type2(study4, mt4)
  print("list: "+str(study4))
  print("type 1 expected: ([1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 30, 40)")
  print(f" Actual Type 1: {type1_result4}")
  print("type 2 expected: ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.8666666666666667, 1, 1], 43, 57.333333333333336)")
  print(f" Actual Type 2: {str(type2_result4)}")
  '''

  #uncomment below for runtime tests for part1
  '''
  maxTime=[10,100,250,500,750,1000,2500,5000,7500,10000]
  for size in maxTime:
    chapList=[]*size
    for i in range(size):
      chapList.append((i+1,i+1))

    print("~TYPE 1 Runtime for list of " + str(size) + " length: " + str(timeit.timeit(stmt=lambda: StudyGuide.getBestGuide_type1(chapList,size), number=1)))
    print("~TYPE 2 Runtime for list of " + str(size) + " length: " + str(timeit.timeit(stmt=lambda: StudyGuide.getBestGuide_type2(chapList, size), number=1)))
  '''


  #uncomment below to run test cases for part 2
  '''
  print("=" * 10)
  print("Part 2: Max Sums")
  print("TEST CASES")

  print("~~~TEST 1~~~")
  #Tests that root value is returned when root is only node in tree
  tree1 = MaxSum.Node(left=None, right=None, item=3)
  result1 = MaxSum.max_sum(tree1)
  print("tree has 1 level")
  print("expected result: 3")
  print("actual result: "+str(result1))

  print("~~~TEST 2~~~")
  # Tests that ensures code generally works. Each level's nodes all have values greater than any node in previous level
  tree2 = MaxSum.generate_example_tree2()
  result2 = MaxSum.max_sum(tree2)
  print("tree has 3 levels")
  print("expected result: 76")
  print("actual result: " + str(result2))

  print("~~~TEST 3~~~")
  # Tests that None is returned if tree is imperfect and thus an invalid input
  tree3 = MaxSum.generate_example_tree3()
  result3 = MaxSum.max_sum(tree3)
  print("tree has 5 levels")
  print("expected result: None")
  print("actual result: " + str(result3))

  print("~~~TEST 4~~~")
  # Tests that None is returned if tree is imperfect and thus an invalid input
  tree4 = MaxSum.generate_example_tree4()
  result4 = MaxSum.max_sum(tree4)
  print("tree has 8 levels")
  print("expected result: -219")
  print("actual result: " + str(result4))
  '''

  #uncomment below for runtime tests for part 2
  '''
  treeSize = [10,100,500,1000,2500,5000,7500,10000,50000,100000,500000,1000000]
  for size in treeSize:
    treeQ = []
    treeRoot = 0
    for i in range(size):
      if i == 0:
        treeRoot = MaxSum.Node(left=MaxSum.Node(item=-5),right=MaxSum.Node(item=-5))
        levelCount =2
        treeL = treeRoot.left
        treeR= treeRoot.right
      treeL.left = MaxSum.Node(item=-5)
      treeL.right = MaxSum.Node(item=-5)
      treeR.left = treeL.right
      treeR.right = MaxSum.Node(item=-5)
      treeL = treeL.left
      treeR = treeR.right

    print("Runtime for tree with " + str(size) + " nodes: " + str(timeit.timeit(stmt=lambda: MaxSum.max_sum(treeRoot), number=1)))
  '''











