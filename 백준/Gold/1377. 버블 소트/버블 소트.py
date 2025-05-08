import sys

N=int(sys.stdin.readline())
numbers=list(int(sys.stdin.readline()) for _ in range(N))
numbers=[[numbers[i],i] for i in range(N)]
sorted_numbers=sorted(numbers)
answer=1
for i in range(N):
    answer=max(answer,sorted_numbers[i][1]-i+1)

print(answer)