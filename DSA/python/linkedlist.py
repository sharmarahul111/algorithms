class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, headValue=None):
        self.head = Node(headValue)
        self.tail = self.head
        self.index = 0
        self.iter_node = self.head

    def __str__(self):
        s = "LinkedList ("
        next = self.head
        while next is not None:
            if type(next.value) is str:
                s += f'"{next.value}"'
            else:
                s += str(next.value)
            if next.next is not None:
                s += " -> "
            next = next.next
        s += ")"
        return s

    def __iter__(self):
        self.index = 0
        self.iter_node = self.head
        return self

    def __next__(self):
        if self.iter_node is None:
            raise StopIteration
        return_value = self.iter_node.value
        self.iter_node = self.iter_node.next
        return return_value

    def append(self, value, next=None):
        self.tail.next = Node(value, next)
        self.tail = self.tail.next

    def prepend(self, value, next=None):
        self.head = Node(value, self.head)

    def pop(self):
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        return_value = curr.next.value
        curr.next = None
        return return_value

    def pop_head(self):
        if self.head:
            return_value = self.head.value
            self.head = self.head.next
            return return_value

    def clear(self):
        self.head = None


if __name__ == "__main__":
    a = LinkedList(10)
    a.append(20)
    a.append(40)
    a.prepend("Houli")
    print()
    print("Iterating:")
    for i in a:
        print(i)
    print()
    print("After prepend: ", a)
    print("After pop:", a.pop(), a)
    print("Pop head:", a.pop_head(), a)
    a.clear()
    print("After clear:", a)
