stack = []

def push(item):
    stack.append(item)

def pop():
    return stack.pop(len(stack)-1)

def peek():
    return stack[len(stack)-1]

def isEmpty():
    if (len(stack)==0):
        return True
    else:
        return False

def size():
    return len(stack)





