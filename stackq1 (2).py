stack1 = []
stack2 = []
stack_e1 = []
stack_e2 = []

def push(stack_id,e):
    stack_id.append(e)

def pop(stack_id):
    return stack_id.pop()

push(stack1,'a')
push(stack1,'b')
push(stack1,'c')
push(stack1,'d')

print(stack1)

while(len(stack1)>0):
    push(stack_e1,pop(stack1))
print ('stack e1 = ')
print (stack_e1)

while(len(stack_e1)>0):
    push(stack_e2,pop(stack_e1))
print ('stack e2 = ')
print (stack_e2)

while(len(stack_e2)>0):
    push(stack2,pop(stack_e2))
print ('stack 2 = ')
print (stack2)
