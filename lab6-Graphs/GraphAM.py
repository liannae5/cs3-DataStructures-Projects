class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.am = [([0]*vertices) for i in range(vertices) ]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AM'
        
    def insert_edge(self, source, dest, weight=1):
        if 0 <= source < len(self.am) and 0 <= dest < len(self.am):
            if weight != 1 and not self.weighted:
                print('Error, inserting weighted edge to unweighted graph')
            else:
                self.am[source][dest] = weight
                if not self.directed:
                    self.am[dest][source] = weight
        else:
            print('Error, vertex number out of range')
        
    def delete_edge(self, source, dest):
        if 0 <= source < len(self.am) and 0 <= dest < len(self.am):
            self.am[source][dest] = -1
            if not self.directed:
                self.am[dest][source] = -1
        else:
            print('Error, vertex number out of range')
            
                
    def display(self):
        print(self.am)

    def num_vertices(self):
        return len(self.am)
