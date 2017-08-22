queue = []

def enqueue(e):
    queue.append(e)

def dequeue():
    return queue.pop(0)

enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)

print(queue)

dequeue()

print(queue)
