
class PriorityNode:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

class MinPriorityQueue:

    def __init__(self):
        self.queue = list()

    def push(self, name, priority):
        node = PriorityNode(name, priority)
        self.delete_if_exists(name)

        if self.is_empty():
            self.queue.append(node)
        else:
            for i in range(0, self.size()):
                if node.priority >= self.queue[i].priority:
                    if i == self.size() - 1:
                        self.queue.insert(i + 1, node)
                    else:
                        continue
                else:
                    self.queue.insert(i, node)

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def print(self):
        for x in self.queue:
            print (str(x.name) + " - " + str(x.priority))

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size()==0

    def delete_if_exists(self, name):
        index_of_existing_node = -1
        for i in range(0, self.size()):
            if self.queue[i].name == name:
                index_of_existing_node = i
        if index_of_existing_node > -1:
            self.queue.pop(index_of_existing_node)