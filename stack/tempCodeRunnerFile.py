stack=[]
    for i in range(len(operations)): 
        if(operations[i]=='+'):
            stack.append(stack[len(stack)-1]+stack[len(stack)-2])
        elif(operations[i]=='D'):
            stack.append(stack[len(stack)-1]*2)
        elif(operations[i]=='C'):
            stack.pop()
        else:
         stack.append(int(operations[i]))
    count=0
    for i in range(len(stack)):
        count+=stack[i]
    return count