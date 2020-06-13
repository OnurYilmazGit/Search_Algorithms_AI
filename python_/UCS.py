from Node import Node
import queue as Q


class UCS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = list()
        self.queue = Q.PriorityQueue()
        self.counter = 0
        self.visited.append(root.UID)
        self.queue.put(root)

    def run(self, target):
        """ YOUR CODE HERE """
        while self.queue:
            node = self.queue.get()
            self.counter += 1

            adjacencyList = (self.graph.reveal_neighbors(node))

            if Node.is_equal(target, node):
                return True, self.counter, node.step

            self.visited.append(node.UID)

            for i in adjacencyList:
                if i.UID not in self.visited:
                    self.queue.put(i)

        return False, 0, 0
