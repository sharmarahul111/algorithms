from linkedlist import LinkedList


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, value):
        self.stack.prepend(value)

    def pop(self):
        return self.stack.pop_head()


if __name__ == "__main__":
    a = Stack()
    a.push(30)
    a.push(20)
    a.push(10)
    print(a.pop())
    print(a.pop())
    print(a.pop())
