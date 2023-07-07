import itertools
import sys

words=[]
answer=[]
for _ in range(6):
    words.append(sys.stdin.readline().rstrip())

p=list(itertools.permutations(words,3))

def check(words2:list, arr):
    for i in range(3):
        tmp=arr[i]
        if tmp in words2:
            words2.remove(tmp)

    for i in range(3):
        tmp=''
        for j in range(3):
            tmp+=arr[j][i]
        if tmp in words2:
            words2.remove(tmp)

    if not words2:
        return True

    return False

for e in p:
    if check(words.copy(),e):
        answer.append(e)


if answer:
    for i in answer[0]:
        print(i)
else:
    print(0)

