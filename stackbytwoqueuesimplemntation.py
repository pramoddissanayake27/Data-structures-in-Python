st = []
qe =  []

def enqueue(s,e):
    s.append(e)

def dequeue(s):
    return s.pop(0)

def size(s):
    return len(s)

def push(e):
    enqueue(st,e)

def pop():
    while(size(st)>1):
        enqueue(qe,dequeue(st))
    x = dequeue(st)
    while(size(qe)>0):
        enqueue(st,dequeue(qe))
    return x

push(1)
push(2)
push(3)
push(4)
