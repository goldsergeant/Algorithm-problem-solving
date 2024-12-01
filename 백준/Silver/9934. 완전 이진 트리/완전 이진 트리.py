import sys


def set_level(left, right, depth):
    if left == right:
        level[depth].append(nums[left])
        return

    mid=(left + right) // 2
    level[depth].append(nums[mid])
    set_level(left,mid-1,depth+1)
    set_level(mid+1,right,depth+1)

K = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
level = [[] for _ in range(K)]
set_level(0,len(nums)-1,0)

for arr in level:
    print(*arr)