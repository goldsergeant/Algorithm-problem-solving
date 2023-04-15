import sys

l,c=map(int,sys.stdin.readline().split())
arr=list(sys.stdin.readline().split())
visited=[False for _ in range(c)]
answer=[]
vowels=['a','e','i','o','u']
def dfs(depth,string):
    if depth==l:
        vowel_count=0
        cons_count=0
        for st in string:
            if st in vowels:
                vowel_count+=1
            else:
                cons_count+=1

        if vowel_count>=1 and cons_count>=2:
            answer.append(string)
        return

    for i in range(c):
        if not visited[i] and string[-1]<arr[i]:
            visited[i]=True
            dfs(depth+1,string+arr[i])
            visited[i]=False

for i in range(c):
    visited[i]=True
    dfs(1,arr[i])
    visited[i]=False

answer.sort()
for i in answer:
    print(i)