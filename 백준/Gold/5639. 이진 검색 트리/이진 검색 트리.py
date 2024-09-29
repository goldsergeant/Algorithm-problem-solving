import sys
sys.setrecursionlimit(100000)

pre_order = []

while True:
    try:
        pre_order.append(int(sys.stdin.readline()))
    except:
        break

answer=[]

def get_post_order(left,right):
    if left>right:
        return

    answer.append(pre_order[left])
    mid= left+1
    while mid<=right and pre_order[mid]<pre_order[left]:
        mid+=1
    get_post_order(mid,right)
    get_post_order(left+1,mid-1)

get_post_order(0,len(pre_order)-1)

print(*answer[::-1],sep='\n')
