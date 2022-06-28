
#import GraphAL as graph
import GraphAM as graph # Replace line 3 by this one to demonstrate adjacy maxtrix implementation
#import GraphEL as graph # Replace line 3 by this one to demonstrate edge list implementation

import plot_graphAL # Uncomment this to use the Draw functions

if __name__ == "__main__":

    g = graph.Graph(6)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    #plot_graphAL.drawGraphAL(g) #Uncomment to plot using Matplotlib
    input("Press Enter to Continue...")
    g.delete_edge(1,2)
    g.display()
    input("Press Enter to Continue...")
    
    print("second graph")
    g = graph.Graph(6,directed = True)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    #plot_graphAL.drawGraphAL(g) #Uncomment to plot using Matplotlib
    input("Press Enter to Continue...")
    g.delete_edge(1,2)
    g.display()
    input("Press Enter to Continue...") 
    
    g = graph.Graph(6,weighted=True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    #plot_graphAL.drawGraphAL(g) #Uncomment to plot using Matplotlib
    input("Press Enter to Continue...")
    g.delete_edge(1,2)
    g.display()
    input("Press Enter to Continue...")

    g = graph.Graph(6,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    input("Press Enter to Continue...")
    #g.delete_edge(1,2)
    g.display()
    #plot_graphAL.drawGraphAL(g) #Uncomment to plot using Matplotlib
    input("Press Enter to Continue...")
        

