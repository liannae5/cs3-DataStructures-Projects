'''
**NOTE: I did not change any of the code or the report for this lab resubmission.
I am only resubmitting to gain the points lost from initially submitting my work late.
'''

'''
CS 2302
Lab 6: Graphs
theSpy.py

Student Name: Lianna Estrada
Student ID: 80642079
Last Modified: 4/24/2022
'''
import timeit

def findSpy(trust):
    notSpy = set() #filled with each vertex that isn't the spy
    nSet = set()
    person = 0
    #finds how many people(n) there are by checking each tuple for new person
    for i in trust:
        if (i[0] not in nSet) and i[0] not in notSpy: #if x is not in nSet add it
            nSet.add(i[0])
            notSpy.add(i[0]) #i[0] = x. if a vertex is x, it trusts someone and cannot be the Spy

        if(i[1] not in nSet): #if y is not in nSet, add it
            nSet.add(i[1])

        if i[0] == i[1] and i[0] not in notSpy: #if vertex trusts itself add to notSpy
            notSpy.add(i[0])

    n = len(nSet) #n = number of unique vertices (people)

    #if len(notSpy) = n, that means every person trusts at least one other person and there is no spy
    #if len(notSpy) < n-1, that means there is more than 1 person that doesn't trust anyone and there is no spy
    if len(notSpy) == n or len(notSpy) < (n-1):
        return -1 #return -1 when there is no spy

    person = 1 #holds person's number
    #iterates through each person(vertex)
    while person < n+1:
        #if person is in notSpy set, it does not need to be checked who trusts them
        if person in notSpy:
            person += 1 #increase person number
            continue #stop and go to next loop iteration
        trustCount = 0 #number of people that trust potential spy
        for i in trust:

            # if trustCount = n-1, that means everyone except the spy(person) trusts the spy and thus there is a spy
            if trustCount == n-1:
                return person #return spy's number, break out of the loop

            #if y = person increase trust count
            if person == i[1]:
                trustCount += 1
        #checks trust count for proper number incase last tuple in list contained y that made trustCount = n-1
        if trustCount == n - 1:
            return person #There is a spy, so return spy's number

    return -1 #if not everyone besides the spy trusted the spy (trustCount < n), then there is no spy

if __name__ == "__main__":

    #Test cases, uncomment below to run

    #Tests that method works when non-spy vertices trust other vertices beside the spy
    print("-----TEST 1-----")
    test1L = [(1,3),(2,3),(4,3),(5,3),(1,4),(4,1),(2,4),(5,2)]
    print("List :"+str(test1L))
    test1res = findSpy(test1L)
    print("expected spy vertex: " + str(3))
    print("test 1 result: "+str(test1res))
    
    #Tests that method returns no spy when more than one vertex doesn't trust any other vertex
    print("-----TEST 2-----")
    test2L = [(2,1),(1,3),(4,6),(1,8),(4,8),(6,7),(2,8),(3,8),(7,6),(7,8),(6,8),(7,5)]
    print("List: "+str(test2L))
    test2res = findSpy(test2L)
    print("expected spy vertex: " + str(-1))
    print("test 2 result: "+str(test2res))
    
    #Tests that method returns no spy when every vertex trusts at least one other vertex
    print("-----TEST 3-----")
    test3L = [(1,2),(2,4),(4,3),(3,1),(2,3),(3,2)]
    print("List: "+str(test3L))
    test3res = findSpy(test3L)
    print("expected spy vertex: " + str(-1))
    print("test 3 result: "+str(test3res))
    
    #Tests that method returns a spy when all other vertices only trust the spy
    print("-----TEST 4-----")
    test4L = [(1,7),(2,7),(3,7),(4,7),(5,7),(6,7)]
    print("List: "+str(test4L))
    test4res = findSpy(test4L)
    print("expected spy vertex: "+ str(7))
    print("test 4 result: " + str(test4res))


    #Runtime tests, uncomment below to run
    '''
    numV = [11,101,301,501,701,1001,2001,3001,4001,5001,7001,10001]
    for i in numV:
        index = 1
        testList = []
        while index < i:
            if index == i-1:
                index+=1
                continue
            testList.append((index,i-1))
            index += 1
        print("Runtime for graph with " + str(i-1) + " vertices: " + str(timeit.timeit(stmt=lambda: findSpy(testList), number=1)))
    '''






