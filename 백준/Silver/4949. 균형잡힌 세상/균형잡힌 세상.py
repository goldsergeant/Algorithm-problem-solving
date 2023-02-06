import sys

while True:
    s=sys.stdin.readline()
    if s=='.\n':
        break
    stack=[]
    for char in s:
        if char=='(':
            stack.append('(')
        elif char=='[':
            stack.append('[')
        elif char==')':
            if len(stack)>0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(1)
                break
        elif char==']':
            if len(stack)>0 and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(1)
                break
    print('yes' if len(stack)==0 else 'no')
