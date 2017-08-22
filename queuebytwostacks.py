q = []
se = []

def push(s,e):
    s.append(e)

def pop(s):
    return s.pop(len(s)-1)

def size(s):
    return len(s)

# def enqueue(e):
#    push(q,e)

# def dequeue():
#    while(size(q)>0):
#        push(se,pop(q))
#    x = pop(se)
#    while(size(se)>0):
#        push(q,pop(se))
#    return x

def enqueue(e):
    while(size(se)>0):
        push(q,pop(se))
    push(q,e)

def dequeue():
    while(size(q)>0):
        push(se,pop(q))
        
    return pop(se)

enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)        
    
