
class PriorityNode:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

class MinPriorityQueue:

    def __init__(self):
        self.queue = list()

    def push(self, name, priority):
        node = PriorityNode(name, priority)
        if self.is_empty():
            self.queue.append(node)
        else:
            for i in range(0, self.size()):
                if node.priority >= self.queue[i].priority:
                    if i == self.size() - 1:
                        self.queue.insert(i + 1, node)
                        break
                    else:
                        continue
                else:
                    self.queue.insert(i, node)
                    break

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

