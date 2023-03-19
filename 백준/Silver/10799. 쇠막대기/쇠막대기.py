s=input()
stack=[]
sticks=[]
answer=0
for i in range(len(s)):
    if s[i]=='(':
        if s[i+1]==')':
            answer+=len(stack)
        else:
            stack.append(i)
    elif s[i]==')':
        if s[i-1]!='(':
            start=stack.pop()
            end=i
            sticks.append((start,end))

print(answer+len(sticks))
