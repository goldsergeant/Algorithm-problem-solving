import collections
import sys

N,K=map(int,sys.stdin.readline().split())
electronic_items=list(map(int,sys.stdin.readline().split()))
cur_set=set()
answer=0
for i in range(len(electronic_items)):
    if len(cur_set)<N:
        cur_set.add(electronic_items[i])
    elif electronic_items[i] not in cur_set:
        later_idx=dict()
        for j in range(i+1,len(electronic_items)):
            if electronic_items[j] not in later_idx:
                later_idx[electronic_items[j]]=j

        pop_item=-1
        later=-1
        for cur_item in cur_set:
            if later<later_idx.get(cur_item,sys.maxsize):
                pop_item=cur_item
                later=later_idx.get(cur_item,sys.maxsize)

        cur_set.remove(pop_item)
        cur_set.add(electronic_items[i])
        answer+=1

print(answer)