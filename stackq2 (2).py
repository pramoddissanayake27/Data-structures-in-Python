s1 = ['a','b','c','d']
se = []
s2 = []

def push(si,e):
    si.append(e)

def pop(si):
    return si.pop(len(si)-1)

print ('s1')
print (s1)

while(len(s1)>0):
    push(se,pop(s1))

print ("se")
print (se)

while(len(se)>0):
    push(s2,pop(se))

print ('s2')
print (s2)
