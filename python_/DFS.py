from Node import Node 

class DFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = list()
        self.stack = list()
        self.stack.append(root)
        self.counter = 0
        self.visited.append(root.UID)

    def run(self, target):
        
        while self.stack:
            self.counter += 1 
            current = self.stack.pop()         
           
            adjacencyList = (self.graph.reveal_neighbors(current))

            if Node.is_equal(target, current):
                return True, self.counter, current.step
         
            self.visited.append(current.UID)
         
            for i in adjacencyList:
                if i.UID not in self.visited:
                    self.stack.append(i)   


        return False, 0, 0 
