import sys

n, t = map(int, sys.stdin.readline().split())
answer=-1
l_arr = []
r_arr = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l_arr.append(a)
    r_arr.append(b)


def check(num):
    tmp = 0
    total_drink = 0
    for i in range(n):
        if l_arr[i] > num:
            return False
        total_drink += l_arr[i]
        tmp += min(r_arr[i], num) - l_arr[i]

    return tmp >= (t - total_drink)

if t<sum(l_arr) or t>sum(r_arr):
    print(-1)
    exit()

left = min(l_arr)
right = max(r_arr)

while left <= right:
    mid = (left + right) // 2

    if check(mid):
        right=mid-1
        answer=mid
    else:
        left=mid+1

print(answer)
