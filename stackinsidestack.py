stack = [[],[],[]]

def push(i,e):
    stack[i].append(e)

def pop(i):
    return stack[i].pop(len(stack[i])-1)

def peek(i):
    return stack[i][len(stack[i])-1]

def isEmpty(i):
    if (len(stack[i])==0):
        return True
    else:
        return False

def size(i):
    return len(stack[i])

push(0,1)
push(0,2)

push(1,10)
push(1,9)
push(1,8)

push(2,4)
push(2,5)
push(2,6)
push(2,7)
