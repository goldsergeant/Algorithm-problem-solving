import sys

a_size, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
answer=[]
def merge(p, q, r):
    if r-p==0:
        return
    i = p
    j = q + 1
    t = 0
    tmp = [0 for i in range(r-p+1)]
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]  # tmp[t] <- A[i]; t++; i++;
            t += 1
            i += 1
        else:
            tmp[t] = arr[j]  # tmp[t] <- A[j]; t++; j++;
            t += 1
            j += 1

    while i <= q:  # 왼쪽 배열 부분이 남은 경우
        tmp[t] = arr[i]
        t += 1
        i += 1
    while j <= r:  # 오른쪽 배열 부분이 남은 경우
        tmp[t] = arr[j]
        t += 1
        j += 1
    i = p
    t = 0
    while i <= r:  # 결과를 A[p..r]에 저장
        arr[i] = tmp[t]
        answer.append(tmp[t])
        if len(tmp)==k:
            print(tmp[t])
            return
        i += 1
        t += 1



def merge_sort(p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort( p, q)
        merge_sort( q + 1, r)
        merge( p, q, r)


merge_sort(0, len(arr)-1)
print(answer[k-1] if len(answer)>=k else -1)
