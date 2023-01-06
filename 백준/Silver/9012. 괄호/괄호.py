import collections

n=int(input())
for i in range(n):
    stack=collections.deque()
    st=input()
    for char in st:
        if char=='(':
            stack.append(char)
        else:
            if len(stack)==0:
                stack.append(char)
                break
            else:
                stack.pop()
    print("YES" if len(stack)==0 else "NO")