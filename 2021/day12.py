'''
26 April 2022
PART 1 ANSWER - 4754
PART 2 ANSWER - 

Concepts: Graphs, stacks, recursion, graph depth
'''
import os
from operator import xor

class Graph:
    
    # Constructor
    def __init__(self):
        self.graph = {}
        self.paths = []
    
    # Add to dictionary
    def addEdge(self,u,v):
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)
        
    # Recursive function to go down
    def DFSUtil(self, cave, stack, visited):
        still_left = [neighbors for neighbors in self.graph[cave]]
        while len(still_left) > 0:
            if cave == 'end':
                self.paths.append(stack)
                return
            if still_left[0] not in visited:
                if cave.islower(): # Part 1 statement
                    self.DFSUtil(still_left[0], stack + [still_left[0]], visited + [cave])
                else:
                    self.DFSUtil(still_left[0], stack + [still_left[0]], visited)
            still_left.pop(0)
        
    # lil wrapper
    def DFS(self, cave):
        self.DFSUtil(cave,[],[] +[cave])
    
    def to_string(self):
        for n,path in enumerate(self.paths):
            print("Path %i:"%(n+1),path)

def main():
    input_path = 'C:\\Users\\cdejo\\Desktop\\Coding\\PythonPrograms\\AdventOfCode\\2021\\inputs\\'
    array = [x.strip() for x in open(input_path+os.path.basename(__file__).split('.')[0]+'.txt', 'r')]
    
    g = Graph()
    STARTING_CAVE = 'start'
    
    for l in array:
        e1,e2 = l.split('-')
        g.addEdge(e1,e2)
        g.addEdge(e2,e1)
    
    g.DFS(STARTING_CAVE)
    print('Total: %i'%len(g.paths))
main()