import sys

input = sys.stdin.readline

N,K = map(int,input().split())
A = list(map(int, input().split()))

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    tmp = []
    i = p
    j = q + 1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1

    global K
    for i in range(p, r + 1):
        K-=1
        A[i] = tmp[i - p]
        if K==0:
            print(*A)
            exit()

merge_sort(A, 0, N - 1)
print(-1)