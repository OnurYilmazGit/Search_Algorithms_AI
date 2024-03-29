import queue as Q
from Node import Node

class AStar:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.visited = list()
        self.queue = Q.PriorityQueue()
        self.counter = 0
        self.visited.append(root.UID)
        self.queue.put(root)
        

    def run(self, target):
        """ YOUR CODE HERE """
        max_search_depth = 0
        while self.queue:
            node = self.queue.get()
            self.counter += 1

            if Node.is_equal(target,node):
                return True, self.counter, node.step 
            
            self.visited.append(node.UID)
            adjacencyList = (self.graph.reveal_neighbors(node))

            for i in adjacencyList:
                if i.UID not in self.visited:
                    self.queue.put(i)
                    distance = self.manhattan_distance(i,target)
                    if distance > max_search_depth:
                        max_search_depth = distance
                elif i.UID in self.visited:
                    if self.manhattan_distance(i,target) < self.manhattan_distance(node,target):
                        self.queue.put(i)

            
        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

    def manhattan_distance(self, node, end):
        arr = [0] * (self.graph.size + 1)
        brr = [0] * (self.graph.size + 1)
        for i in range(len(node.g_node)):
            for j in range(len(node.g_node[i])):
                arr[node.g_node[i][j]] = [i, j]

        for i in range(len(end.g_node)):
            for j in range(len(end.g_node[i])):
                brr[end.g_node[i][j]] = [i, j]
        dist = 0
        for i in range(1, len(arr)):
            dist += abs(arr[i][0] - brr[i][0]) + abs(arr[i][1] - brr[i][1])
        return dist
