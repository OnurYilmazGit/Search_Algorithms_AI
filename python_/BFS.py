from Node import Node

class BFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = list()
        self.queue = list()
        self.counter = 0
        self.visited.append(root.UID)
        self.queue.append(root)
        

    def run(self, target):
        
        while self.queue:
            self.counter += 1
            current = self.queue[0]
            self.queue.pop(0)
            
            adjacencyList = (self.graph.reveal_neighbors(current))

            ''' Check for inital is equal to target on first step '''
            if Node.is_equal(target, current):
                return True, self.counter, current.step
           
            self.visited.append(current.UID)
            ''' First step for adding top Node to visited node '''
            for i in adjacencyList:
                if i.UID not in self.visited:
                    self.queue.append(i)

        return False, 0, 0 
