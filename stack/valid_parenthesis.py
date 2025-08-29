def valid_parenthesis(s):
    stack=[]
    for i in range(len(s)):
        if len(s)==1  :
            return False
        if s[i] in '({[':
            stack.append(s[i])
            print(stack)
       
        else:
            item=stack[len(stack)-1]
            if (item=='(' and s[i]==')') or (item=='{' and s[i]=='}') or (item=='[' and s[i]==']'):
                stack.pop()
                print(stack)
            else:
                return False
    if len(stack)>=1:
        return False
    else:
      return True
print(valid_parenthesis('()'))
