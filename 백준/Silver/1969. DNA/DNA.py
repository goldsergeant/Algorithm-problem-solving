import collections
import sys

n,m=map(int,input().split())
dna=[]
answer=''
hamming_distance=0
for _ in range(n):
    dna.append(sys.stdin.readline().rstrip())

for col in range(m):
    counter=collections.Counter()
    for row in range(n):
        counter[dna[row][col]]+=1

    tmp=counter.most_common(n)
    tmp.sort(key=lambda x:x[0])
    tmp.sort(key=lambda x:x[1],reverse=True)
    answer+=tmp[0][0]
    hamming_distance+=n-tmp[0][1]


print(answer)
print(hamming_distance)