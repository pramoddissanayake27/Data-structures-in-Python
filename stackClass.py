class Stack:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return repr(self.items)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self,val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

s1 = Stack()
s2 = Stack()

print(s1.isEmpty())
print(s2.isEmpty())

s1.push(1)
s2.push(0)
s1.push(2)
s2.push(9)
s1.push(3)

print(s1.isEmpty())
print(s2.isEmpty())

print(s1)
print(s2)
