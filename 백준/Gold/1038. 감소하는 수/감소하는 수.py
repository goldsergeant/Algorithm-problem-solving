from itertools import combinations
n=int(input())
answer=[]
for i in range(1,11):
    for j in combinations(range(10),i):
        answer.append(''.join(map(str,reversed(list(j)))))

answer.sort(key=lambda x:int(x))

print(answer[n] if n < len(answer) else -1)

