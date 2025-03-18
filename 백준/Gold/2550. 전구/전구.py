import sys
from bisect import bisect_left
from locale import locale_encoding_alias

N=int(sys.stdin.readline())
switches=[0]+list(map(int,sys.stdin.readline().split()))
buttons=[0]+list(map(int,sys.stdin.readline().split()))
button_numbers=[0 for _ in range(N+1)]
reverse_tracking=[0 for _ in range(N+1)]

num=0
for b in buttons:
    button_numbers[b]=num
    num+=1

arr=[button_numbers[switches[1]]]
for i in range(2,N+1):
    if arr[-1]<button_numbers[switches[i]]:
        arr.append(button_numbers[switches[i]])
        reverse_tracking[i]=len(arr)-1
    else:
        idx=bisect_left(arr,button_numbers[switches[i]])
        arr[idx]=button_numbers[switches[i]]
        reverse_tracking[i]=idx

answer_switches=[]

cur=len(arr)-1
for i in range(N,-1,-1):
    if reverse_tracking[i]==cur:
        answer_switches.append(switches[i])
        cur-=1
print(len(arr))
print(*sorted(answer_switches))