import sys
from itertools import combinations, permutations

def convert_string(idxs):
    tmp = []
    can_put = [True for _ in range(len(string))]
    for i in idxs:
        can_put[i] = False

    for i in range(len(string)):
        if can_put[i]:
            tmp.append(string[i])

    return ''.join(tmp)

answer = set()
string = list(sys.stdin.readline().rstrip())
parenthesis_pairs=[]
stack=[]

for idx,ch in enumerate(string):
    if ch=='(':
        stack.append(idx)
    elif ch==')':
        i=stack.pop()
        parenthesis_pairs.append((i,idx))

for cnt in range(1,len(parenthesis_pairs)):
    for case in combinations(parenthesis_pairs,cnt):
        idxs=[]
        for tup in case:
            idxs.extend(tup)
        answer.add(convert_string(idxs))

idxs=[]
for tup in parenthesis_pairs:
    idxs.extend(tup)
answer.add(convert_string(idxs))

print(*sorted(answer),sep='\n')