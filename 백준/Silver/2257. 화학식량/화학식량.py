s=input()
dic={'H':1,'C':12,'O':16}
stack=[]
for i in range(len(s)):
    if s[i]=='(':
        stack.append('(')
    elif s[i]==')':
        num=0
        while True:
            target=stack.pop()
            if target=='(':
                break

            num+=target
        stack.append(num)

    elif s[i] in dic.keys():
        stack.append(dic[s[i]])

    else:
        stack[-1]=stack[-1]*int(s[i])

print(sum(stack))
