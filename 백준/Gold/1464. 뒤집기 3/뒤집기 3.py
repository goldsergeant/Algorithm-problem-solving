import collections

s=input()
q=collections.deque()
for i in range(len(s)):
    if not q:
        q.append(s[i])
    else:
        if s[i]<=q[0]:
            q.appendleft(s[i])
        elif s[i]>=q[-1]:
            q.append(s[i])
        else:
            q.append(s[i])

print(''.join(q))