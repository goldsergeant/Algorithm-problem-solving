import sys

S=input()
stack=[]
for char in S:
    if char==')':
        if stack and stack[-1]=='(':
            stack.pop()
        else:
            stack.append(')')
    else:
        stack.append('(')

print(len(stack))