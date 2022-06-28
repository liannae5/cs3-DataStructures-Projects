# Adjacency list representation of graphs

class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'
        
    def insert_edge(self, source, dest, weight=1):
        if source >= len(self.al) or dest >= len(self.al) or source < 0 or dest < 0:
            print('Error, vertex number out of range')
        elif weight != 1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest, weight)) 
            if not self.directed:
                self.al[dest].append(Edge(source, weight))

    
    def delete_edge_(self,source,dest):
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i +=1
        return False
    
    def delete_edge(self,source,dest):
        if 0 <= source < len(self.am) and 0 <= dest < len(self.am):
            deleted = self.delete_edge_(source, dest)
            if not self.directed:
                deleted = self.delete_edge_(dest, source)
            if not deleted:        
                print('Error, edge to delete not found')
        else:
            print('Error, vertex number out of range')
            
    def display(self):
        print('[', end='')
        for adj in self.al:
            print('[', end='')
            for edge in adj:
                print(f'({str(edge.dest)},{str(edge.weight)})', end='')
            print(']', end=' ')    
        print(']')
    def num_vertices(self):
        return len(self.al)