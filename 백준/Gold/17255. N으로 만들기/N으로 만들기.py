import sys


def dfs(left, right):
    if left == right:
        return 1,N[left]

    st = N[left:right + 1]
    if st in cache.keys():
        return cache[st]

    left_val,left_st=dfs(left+1,right)
    right_val,right_st=dfs(left,right-1)
    if left_st == right_st:
        return left_val,st
    return left_val+right_val,st

N = sys.stdin.readline().rstrip()
cache = dict()
print(dfs(0, len(N) - 1)[0])
