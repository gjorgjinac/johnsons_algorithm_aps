
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
            print(str(x.name) + " - " + str(x.priority))

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0


class MinHeap():

    def __init__(self):
        self.heap = []
        self.size = 0
        self.node_position = {}


    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def find_index_of_smaller_element(self, a, b):
        if a < self.size and b < self.size:
            return a if self.heap[a].priority < self.heap[b].priority else b
        return -1

    def update_heap(self, node_index):
        smallest = self.find_index_of_smaller_element(node_index, 2 * node_index + 1)
        smallest = self.find_index_of_smaller_element(smallest, 2 * node_index + 2)

        if smallest != node_index and smallest!=-1:
            self.node_position[self.heap[smallest].name] = node_index
            self.node_position[self.heap[node_index].name] = smallest
            self.swap(smallest, node_index)
            self.update_heap(smallest)


    def pop_min(self):

        if self.is_empty():
            return
        min_node = self.heap[0]

        # Replace root node with last node
        lastNode = self.heap[self.size - 1]
        self.heap[0] = lastNode

        # Update position of last node
        self.node_position[lastNode.name] = 0
        self.node_position[min_node.name] = self.size - 1

        # Reduce heap size and heapify root
        self.size -= 1
        self.update_heap(0)

        return min_node


    def is_empty(self):
        return self.size == 0


    def update_priority(self, node, new_priority):
        position_of_node_to_update = self.node_position[node]
        self.heap[position_of_node_to_update].priority = new_priority

        # O(logN)
        while position_of_node_to_update > 0 and self.heap[position_of_node_to_update].priority < self.heap[(position_of_node_to_update - 1) // 2].priority:
            # swap node with parent
            self.node_position[self.heap[position_of_node_to_update].name] = (position_of_node_to_update - 1) // 2
            self.node_position[self.heap[(position_of_node_to_update - 1) // 2].name] = position_of_node_to_update
            self.swap(position_of_node_to_update, (position_of_node_to_update - 1) // 2)

            # move to parent index
            position_of_node_to_update = (position_of_node_to_update - 1) // 2


    def contains(self, node):
        return self.node_position[node] < self.size

    def print(self):
        for i in self.heap:
            print(f'{i.name}   {i.priority}')
