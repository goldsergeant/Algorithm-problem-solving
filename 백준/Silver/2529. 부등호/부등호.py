import sys

k=int(input())
signs=list(sys.stdin.readline().split())
visited=[False for _ in range(10)]
answer=[]

def check(numbers)->bool:
    for i in range(len(numbers)-1):
        if signs[i]=='<':
            if not(numbers[i]<numbers[i+1]):
                return False
        else:
            if not(numbers[i]>numbers[i+1]):
                return False
    return True


def dfs(numbers):
    if len(numbers)==k+1:
        if check(numbers):
            answer.append(numbers)
        return

    for i in range(10):
        if not visited[i]:
            visited[i]=True
            dfs(numbers+str(i))
            visited[i]=False

for i in range(10):
    visited[i]=True
    dfs(str(i))
    visited[i]=False

print(answer[-1])
print(answer[0])