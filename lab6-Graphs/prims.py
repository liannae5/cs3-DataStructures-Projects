'''
**NOTE: I did not change any of the code or the report for this lab resubmission.
I am only resubmitting to gain the points lost from initially submitting my work late.
'''

'''
CS 2302
Lab 6: Graphs
prims.py

Student Name: Lianna Estrada
Student ID: 80642079
Last Modified: 4/24/2022
'''
import timeit

import GraphAL as graphL
import GraphAM as graphM
import heapq
import plot_graphAL
def primsMST(graph, u):  # u = arbitraty, initial vertex


    minimum_spanning_tree = set() #MST set
    minimum_spanning_tree.add((u,0)) #add u to MST with weight zero
    connected = set()#set to keep track of vertices already connected
    connected.add(u) #add u to connected
    costHeap = heapq #using heapq to create minHeap
    cHeapL = [] #costHeap list
    costHeap.heappush(cHeapL,[0,u]) #push u into heap with weight of 0

    if graph.representation == 'AL': #method for adjacency list representation
        #add each vertex besides u to the heap
        for v in range(len(graph.al)):
            if v==u:
                continue
            costHeap.heappush(cHeapL,[1e7,v]) #[weight, vertex]. set weight to 1e7 (infinity in this case)
        #iterates through each vertex until all are vertices are connected
        while len(connected) != graph.num_vertices():
            #if costHeap is empty, then we are done
            if len(cHeapL) == 0:
                break
            currV = costHeap.heappop(cHeapL) #pop costHeap to get next vertex to check

            currV[0] = 1e7 #set currV's weight to infinity

            minVert = currV[1] #set minVert to currV
            minWeight = currV[0] #set minWeight to currV weight

            #check for minimum edge weight
            for vert in graph.al[currV[1]]:
                #if vert is not already connected and the edge weight < minWeight
                if vert.dest not in connected and vert.weight < minWeight:
                    minVert = vert.dest #update minVert
                    minWeight = vert.weight #update minWeight
                    costHeap.heappush(cHeapL, [minWeight, minVert]) #push min vert and weight to Heap
            #add minVert to MST as long as currV is connected to other vertex in graph and minWeight not infinity
            if len(graph.al[currV[1]]) != 0 and minWeight != 1e7:
                minimum_spanning_tree.add((currV[1],minVert,minWeight)) #MST element stored as (source,dest,weight)
            connected.add(minVert) #add minVert to connected

    else: #method for adjacency matrix representation
        #add are vertices besides u to Heap
        for v in range(len(graph.am)):
            if v==u:
                continue
            costHeap.heappush(cHeapL,[1e7,v]) #1e7 = infinity in this case. Set weight of each vertex to infinity
        # iterates through each vertex until all are vertices are connected
        while len(connected) != graph.num_vertices():
            #if costHeap is empty than we are done
            if len(cHeapL) == 0:
                break
            currV = costHeap.heappop(cHeapL) #pop from costHeap to get next vertex to look at
            currV[0] = 1e7 #set weight to infinity
            minVert = currV[1] #set minVert to currV
            minWeight = currV[0] #set minWeight to currV weight

            #check for minimum edge connected to currV
            for vert in range(len(graph.am[currV[1]])):
                #if vert not already connected, its weight < minWeight and it is connected to currV update minVert and minWeight
                if vert not in connected and graph.am[currV[1]][vert] < minWeight and graph.am[currV[1]][vert] != 0:
                    minVert = vert #update minVert
                    minWeight = graph.am[currV[1]][vert] #update minWeight
                    costHeap.heappush(cHeapL, [minWeight, minVert]) #push minVert and weight onto costHeap
            #if minVert connected to another node in graph and minWeight not infinity, add minVert to MST
            if sum(graph.am[minVert]) != 0 and minWeight != 1e7:
                minimum_spanning_tree.add((currV[1],minVert,minWeight)) #add tuple (src, dest, weight) to MST
            connected.add(minVert) #add minVert to connected


    return minimum_spanning_tree #return MST set

if __name__ == "__main__":
    #Test cases, uncomment below to run

    #Tests when all vertices are connected to each other by at least one edge
    print("-----TEST 1-----")
    print("Adjacency Matrix Representation:")
    gm = graphM.Graph(6, weighted=True)
    gm.insert_edge(0, 1, 4)
    gm.insert_edge(0, 2, 3)
    gm.insert_edge(1, 2, 2)
    gm.insert_edge(2, 3, 4)
    gm.insert_edge(3, 4, 5)
    gm.insert_edge(4, 1, 4)
    print("Matrix: ")
    gm.display()
    gm.insert_edge(3,5,2)
    gm.insert_edge(4,5,4)
    mst = primsMST(gm,4)
    print("expected MST: {(4, 0), (4, 1, 4), (1, 2, 2), (3, 5, 2), (2, 3, 4), (2, 0, 3)}")
    print("here is mst: "+str(mst))


    print("Adjacency List Representation:")
    g = graphL.Graph(6,weighted=True)
    g.insert_edge(0, 1, 4)
    g.insert_edge(0, 2, 3)
    g.insert_edge(1, 2, 2)
    g.insert_edge(2, 3, 4)
    g.insert_edge(3, 4, 5)
    g.insert_edge(4, 1, 4)
    g.insert_edge(3,5,2)
    g.insert_edge(4,5,4)
    print("List: ")
    g.display()
    mst = primsMST(g,4)
    print("expected MST: {(4, 0), (4, 1, 4), (5, 3, 2), (1, 2, 2), (3, 5, 2), (2, 0, 3)}")
    print("here is mst: "+str(mst))
    plot_graphAL.drawGraphAL(g)

    #Tests that no vertex except u is in the MST when contains no edges
    print("-----TEST 2-----")
    print("Adjacency Matrix Representation:")
    gm = graphL.Graph(6, weighted=True)
    print("Matrix: ")
    gm.display()
    mst = primsMST(gm, 2)
    print("expected MST: {(2,0)}")
    print("here is mst: " + str(mst))

    print("Adjacency List Representation:")
    g = graphL.Graph(6, weighted=True)
    print("List: ")
    g.display()
    mst = primsMST(g, 2)
    print("expected MST: {(2,0)}")
    print("here is mst: " + str(mst))

    # Tests when one vertex is not connected by an edge to rest of vertices
    print("-----TEST 3-----")
    print("Adjacency Matrix Representation:")
    gm = graphM.Graph(8, weighted=True)
    gm.insert_edge(0, 1, 4)
    gm.insert_edge(0, 2, 3)
    gm.insert_edge(1, 2, 2)
    gm.insert_edge(2, 3, 4)
    gm.insert_edge(3, 4, 5)
    gm.insert_edge(4, 1, 4)
    print("Matrix: ")
    gm.display()
    gm.insert_edge(3, 5, 2)
    gm.insert_edge(4, 5, 4)
    gm.insert_edge(0,7,6)
    mst = primsMST(gm, 1)
    print("expected MST: {(5, 4, 4), (0, 7, 6), (1, 2, 2), (3, 5, 2), (2, 3, 4), (1, 0), (2, 0, 3)}")
    print("here is mst: " + str(mst))

    print("Adjacency List Representation:")
    g = graphL.Graph(8, weighted=True)
    g.insert_edge(0, 1, 4)
    g.insert_edge(0, 2, 3)
    g.insert_edge(1, 2, 2)
    g.insert_edge(2, 3, 4)
    g.insert_edge(3, 4, 5)
    g.insert_edge(4, 1, 4)
    print("List: ")
    g.display()
    g.insert_edge(3, 5, 2)
    g.insert_edge(4, 5, 4)
    g.insert_edge(0, 7, 6)
    mst = primsMST(g, 1)
    print("expected MST: {(5, 4, 4), (0, 7, 6), (1, 2, 2), (3, 5, 2), (2, 3, 4), (1, 0), (2, 0, 3)}")
    print("here is mst: " + str(mst))

    # Tests when graph is unweighted
    print("-----TEST 4-----")
    print("Adjacency Matrix Representation:")
    gm = graphM.Graph(8, weighted=True)
    gm.insert_edge(0, 1, 4)
    gm.insert_edge(0, 2, 3)
    gm.insert_edge(1, 2, 2)
    gm.insert_edge(2, 3, 4)
    gm.insert_edge(3, 4, 5)
    gm.insert_edge(4, 1, 4)
    print("Matrix: ")
    gm.display()
    gm.insert_edge(3, 5, 2)
    gm.insert_edge(4, 5, 4)
    gm.insert_edge(0, 7, 6)
    mst = primsMST(gm, 1)
    print("expected MST: {(5, 4, 4), (0, 7, 6), (1, 2, 2), (3, 5, 2), (2, 3, 4), (1, 0), (2, 0, 3)}")
    print("here is mst: " + str(mst))

    print("Adjacency List Representation:")
    g = graphL.Graph(8)
    g.insert_edge(0, 1)
    g.insert_edge(0, 2)
    g.insert_edge(1, 2)
    g.insert_edge(2, 3)
    g.insert_edge(3, 4)
    g.insert_edge(4, 1)
    print("List: ")
    g.display()
    g.insert_edge(3, 5)
    g.insert_edge(4, 5)
    g.insert_edge(0, 7)
    mst = primsMST(g, 4)
    print("expected MST: {(0, 7, 1), (4, 0), (4, 3, 1), (2, 0, 1), (3, 2, 1), (3, 5, 1), (0, 1, 1)}")
    print("here is mst: " + str(mst))


    #Runtime tests, uncomment bellow to run
    '''
    numV = [10, 100, 300, 500, 700, 1000, 2000, 3000, 4000, 5000, 7000, 10000]
    for i in numV:
        mGraph = graphM.Graph(i)
        lGraph = graphL.Graph(i)
        for index in range(i-1):
            mGraph.insert_edge(index,index+1)
            lGraph.insert_edge(index,index+1)
        print("Runtime for MATRIX graph with " + str(i) + " vertices: " + str(timeit.timeit(stmt=lambda: primsMST(mGraph,0), number=1)))
        print("Runtime for LIST graph with " + str(i) + " vertices: " + str(timeit.timeit(stmt=lambda: primsMST(lGraph, 0), number=1)))
        '''



