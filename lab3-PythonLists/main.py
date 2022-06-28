'''
CS 2302
Lab 3: Lists
Main.py

Student Name: Lianna Estrada
Student ID: 80642079
Last Modified: 2/28/2022
'''
import random

from SortedList import SortedList
from CircularShift import circularshift_1, circularshift_2
import numpy as np
import matplotlib.pyplot as plt
import time
import timeit
import sys
sys.setrecursionlimit(10**6) #increases recursion limit to test larger data sets

##################################
#       PART 1: Test Code        #
##################################

######### RUNTIME TESTS ##########
#List of input sizes/list sizes to use in part 1 runtime tests
sortinputSizeList = [10,100,500,1000,1500,2000,5000,10000,15000,20000,30000,40000,50000,75000]
for n in sortinputSizeList:
    #print("INPUT SIZE: "+ str(n))

    timeTestList1 = np.random.randint(0,high=80000, size=n,dtype=int)
    #print("test list:"+str(timeTestList1))
    sortList1 = SortedList() #resets sortedList to empty for each input size
    regList1 = [] #resets regList1 to empty for each input size
    sortTime = 0 #resets time to 0
    regTime = 0 #resets time to 0

    #Uncomment to get runtimes for the functions below

    #mechanism to add elements to both lists
    #for i in timeTestList1:
        #regTime += timeit.timeit(stmt=lambda: regList1.append(i), number=1)
        #sortTime += timeit.timeit(stmt=lambda: sortList1.add(i), number=1)

    #add function times
    #print("Addreg: "+str(regTime))
    #print("regular list: "+str(regList1))
    #print("Addsort: "+str(sortTime))
    #print("sorted list: "+str(sortList1))

    #index search times
    #valSearch = timeTestList1[random.randrange(n)]
    #print(str(valSearch))
    #rLsearchTime = timeit.timeit(stmt=lambda: regList1.index(valSearch), number=1)
    #sLsearchTime = timeit.timeit(stmt=lambda: sortList1.indexof(valSearch), number=1)
    #print("Searchreg: "+str(rLsearchTime))
    #print("Searchsort: "+str(sLsearchTime))

    #max function times
    #rLmaxTime = timeit.timeit(stmt=lambda: max(regList1), number=1)
    #sLmaxTime = timeit.timeit(stmt=lambda: sortList1.max(), number=1)
    #print("maxReg: "+str(rLmaxTime))
    #print("maxSort: "+str(sLmaxTime))

######## GENERAL TESTS ##########
gentest1 = SortedList()
orginalList1 = []
for i in range(11):
    randomNum = random.randrange(-10,10)
    orginalList1 += [randomNum]
    gentest1.add(random.randrange(-10,10))

#Uncomment to test Part 1 functions

#print("Unsorted list of random values: "+str(orginalList1))
#print("SortedList: " +str(gentest1))
'''
randomInt = random.randrange(-10,10)
print("Finding indexof with random value " +str(randomInt)+ ": "+str(gentest1.indexof(randomInt)))
print("Finding indexof with list value " +str(gentest1[5])+ ": "+str(gentest1.indexof(gentest1[5])))
print("Testing allunique(): "+str(gentest1.allunique()))
print("Calling popmin(): "+str(gentest1.popmin()))
print("list after popmin(): "+str(gentest1))
print("Calling popmin(): "+str(gentest1.popmin()))
print("list after popmin(): "+str(gentest1))
#print("Calling popmin(): "+str(gentest1.popmin()))
#print("list after popmin(): "+str(gentest1))
print("Result of clearlist: "+ str(gentest1.clear()))
print("Calling max(): "+str(gentest1.max()))
'''

##################################
#       PART 2: Test Code        #
##################################

######## GENERAL TESTS ##########
inputSizeList2 = [7,10,20]
for num in inputSizeList2:
    #print("INPUT SIZE: "+str(num))
    testList2 = np.random.randint(0, high=500, size=num, dtype=int)
    testList2 = list(testList2)
    testList2copy = testList2[:]
    for i in range(3):
        if i == 0:
            k = random.randrange(num-1)
            print("Shift is: "+str(k))
            print("Original list: "+str(testList2))
            print("Circular 1 Shifted list: "+str(circularshift_1(testList2,k)))
            print("Circular 2 Shifted list: " + str(circularshift_2(testList2,k)))
            testList2 = testList2copy[:]
        elif i == 1:
            k = random.randrange(num+1,100)
            print("Shift is: " + str(k))
            print("Actual shift should be: "+str(k%len(testList2)))
            print("Original list: " + str(testList2))
            print("Circular 1 Shifted list: " + str(circularshift_1(testList2,k)))
            print("Circular 2 Shifted list: " + str(circularshift_2(testList2,k)))
            testList2 = testList2copy[:]

        elif i == 2:
            k = random.randrange(-5,-1)
            #print("Shift is: " + str(k))

            #print("Original list: " + str(testList2))
            #print("Circular 1 Shifted list: " + str(circularshift_1(testList2,k)))
            #print("Circular 2 Shifted list: " + str(circularshift_2(testList2,k)))
            testList2 = testList2copy[:]

######### RUNTIME TESTS ##########
#input size list
circinputSizeList = [10,100,500,1000,1500,2000,5000,10000,15000,20000,30000,40000,50000,75000,100000,200000,250000,500000,750000,1000000,2000000]
for n in circinputSizeList:
    #print("INPUT SIZE: "+str(n))
    circular1Time = 0
    circular2Time = 0
    timeTestList2 = np.random.randint(-1000, high=80000, size=n, dtype=int) #generates random list
    timeTestList2 = list(timeTestList2) #had problems with np generated list so I had to type cast it
    timeTestList2copy = timeTestList2[:] #makes list copy
    for i in range(3):
        if i == 0: #runs for k < list length
            k = random.randrange(n-1)
            circular1Time += timeit.timeit(stmt=lambda: circularshift_1(timeTestList2,k), number=1) #updates time for first method
            timeTestList2 = timeTestList2copy[:]
            circular2Time += timeit.timeit(stmt=lambda: circularshift_2(timeTestList2,k), number=1) #updates time for 2nd method
            timeTestList2 = timeTestList2copy[:]
        elif i == 1: #runs for k > list length
            k = random.randrange(n+1,10*n)
            circular1Time += timeit.timeit(stmt=lambda: circularshift_1(timeTestList2,k),number = 1)
            timeTestList2 = timeTestList2copy[:]
            circular2Time += timeit.timeit(stmt=lambda: circularshift_2(timeTestList2,k), number=1)
            timeTestList2 = timeTestList2copy[:]

        elif i == 2: #runs for k < 0
            k = random.randrange(-5,-1)
            circular1Time += timeit.timeit(stmt=lambda: circularshift_1(timeTestList2, k),number = 1)
            timeTestList2 = timeTestList2copy[:]
            circular2Time += timeit.timeit(stmt=lambda: circularshift_2(timeTestList2, k), number=1)
            timeTestList2 = timeTestList2copy[:]

    #uncomment to get runtimes
    #print("circ2 Time: "+str(circular2Time))
    #print("circ1 Time: " + str(circular2Time))
