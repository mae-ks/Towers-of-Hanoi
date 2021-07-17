class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
    
class Stacks:
    def __init__(self, max_size = None):
        self.max_size = max_size
        self.head = None
        self.size = 0

    def has_space(self):
        if self.max_size is None:
            return True
        else:
            return self.size < self.max_size

    def push(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            if self.has_space():
                current = self.head
                new_node.next_node = current
                self.head = new_node
            else:
                print("Overflow")
                return
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            print("Underflow")
            return
        current = self.head
        temp = current
        current = current.next_node
        self.head = current
        self.size -= 1
        return temp.data
    
    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def __repr__(self):
        current = self.head
        arr = []
        while current:
            if current == self.head:
                arr.append("[Top: %s]" %current.data)
            elif current.next_node is None:
                arr.append("[Bot: %s]" %current.data)
            else:
                arr.append("[%s]" %current.data)
            current = current.next_node
        return " -> ".join(arr)

# test = Stacks(3)
# test.push(1)
# test.push(2)
# test.push(3)
# test.push(4)
# test.pop()
# print(test.peek())
# print(test)