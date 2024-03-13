import collections
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(list, sys.stdin.readline().split())
    counter_a = collections.Counter(A)
    counter_b = collections.Counter(B)
    answer = 0
    if counter_a != counter_b:
        print(-1)
        exit()

    a_a_idxs=[]
    b_a_idxs=[]
    for i in range(1,len(A)-1):
        if A[i]=='a':
            a_a_idxs.append(i)
        if B[i]=='a':
            b_a_idxs.append(i)

    for i in range(len(a_a_idxs)):
        answer+=abs(a_a_idxs[i]-b_a_idxs[i])

    print(answer)
