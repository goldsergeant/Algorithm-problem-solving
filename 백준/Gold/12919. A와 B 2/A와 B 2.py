import collections
import sys

s=sys.stdin.readline().rstrip()
t=sys.stdin.readline().rstrip()

def bfs(s,t):
    q=collections.deque([t])
    visited = set()

    while q:
        word=q.popleft()
        if word==s:
            return 1
        if len(word)>=2:
            if word[-1]=='A':
                tmp = word[:-1]
                if tmp not in visited:
                    q.append(tmp)
                    visited.add(tmp)
            if word[0]=='B':
                tmp=word[::-1][:-1]
                if tmp not in visited:
                    q.append(tmp)
                    visited.add(tmp)

    return 0
print(bfs(s,t))