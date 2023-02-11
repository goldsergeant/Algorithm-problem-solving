import collections
import sys

n,m=map(int,sys.stdin.readline().split())
deque=collections.deque(i for i in range(1,n+1))
answer_list=list(map(int,sys.stdin.readline().split()))
count=0
while len(answer_list):
    if deque[0] == answer_list[0]:
        deque.popleft()
        answer_list.pop(0)
    elif deque.index(answer_list[0])<len(deque)/2: #2번 연산
        count+=deque.index(answer_list[0])
        deque.rotate(-deque.index(answer_list[0]))
    elif deque.index(answer_list[0])>=len(deque)/2: #3번 연산
        count+=len(deque)-deque.index(answer_list[0])
        deque.rotate(len(deque)-deque.index(answer_list[0]))
print(count)
