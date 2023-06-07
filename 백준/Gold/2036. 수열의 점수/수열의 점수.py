n=int(input())
positives=[]
negitives=[]
ones=[]
score=0
for _ in range(n):
    num=int(input())
    if num>1:
        positives.append(num)
    elif num<=0:
        negitives.append(num)
    else:
        ones.append(num)

positives.sort(reverse=True)
negitives.sort()

if len(positives)%2==0:
    tmp=0
    for i in range(0,len(positives),2):
        tmp+=positives[i]*positives[i+1]
    score+=tmp
else:
    tmp=0
    for i in range(0,len(positives)-1,2):
        tmp+=positives[i]*positives[i+1]
    tmp+=positives[-1]
    score+=tmp

if len(negitives)%2==0:
    tmp=0
    for i in range(0,len(negitives),2):
        tmp+=negitives[i]*negitives[i+1]
    score+=tmp
else:
    tmp=0
    for i in range(0,len(negitives)-1,2):
        tmp+=negitives[i]*negitives[i+1]
    tmp+=negitives[-1]
    score+=tmp

score+=sum(ones)
print(score)