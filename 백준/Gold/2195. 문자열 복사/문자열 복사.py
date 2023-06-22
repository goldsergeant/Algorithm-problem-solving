S=input()
P=input()
answer=0
idx=0
for i in range(len(P)):
    if P[idx:i+1] not in S:
        idx=i
        answer+=1

print(answer+1)