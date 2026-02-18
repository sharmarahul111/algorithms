class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, headValue=None):
        self.head = Node(headValue)
        self.tail = self.head

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

    def append(self, value, next=None):
        self.tail.next = Node(value, next)
        self.tail = self.tail.next

    def prepend(self, value, next=None):
        self.head = Node(value, self.head)

    def pop(self):
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None

    def pop_head(self):
        if self.head:
            self.head = self.head.next

    def clear(self):
        self.head = None


if __name__ == "__main__":
    a = LinkedList(10)
    a.append(20)
    a.append(40)
    a.prepend("Houli")
    print("After prepend: ", a)
    a.pop()
    print("After pop:", a)
    a.pop_head()
    print("Pop head:", a)
    a.clear()
    print("After clear:", a)
