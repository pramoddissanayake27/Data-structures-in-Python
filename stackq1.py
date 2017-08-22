s1 = ['a','b','c','d']
se1 = []
se2 = []

def push(s,e):
    s.append(e)

def pop(s):
    return s.pop(len(s)-1)

while(len(s1)>0):
    push(se1,pop(s1))

print(se1)

while(len(se1)>0):
    push(se2,pop(se1))

print(se2)

while(len(se2)>0):
    push(s1,pop(se2))

print (s1)
