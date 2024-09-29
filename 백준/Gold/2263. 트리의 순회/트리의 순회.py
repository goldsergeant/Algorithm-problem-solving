import collections
import sys
sys.setrecursionlimit(1000000)

N=int(sys.stdin.readline())
in_order=list(map(int,sys.stdin.readline().split()))
post_order=list(map(int,sys.stdin.readline().split()))
in_order_index_cache=[0 for _ in range(N+1)] # val -> index
for i in range(N):
    in_order_index_cache[in_order[i]]=i

answer=[]

def get_pre_order(in_left, in_right, post_left, post_right):
    if in_left>in_right or post_left>post_right:
        return

    idx = in_order_index_cache[post_order[post_right]]
    left_size=idx-in_left
    answer.append(in_order[idx])

    get_pre_order(in_left, idx - 1, post_left,post_left+left_size-1)
    get_pre_order(idx+1,in_right,post_left+left_size,post_right-1)

get_pre_order(0, N - 1, 0, N - 1)
print(*answer)