exp=input()
nums=exp.split('-')
answer=0
arr=[]
for i in range(len(nums)):
    s=nums[i].split('+')
    tempNum=0
    for j in s:
        tempNum+=int(j.lstrip('0'))
    arr.append(tempNum)

answer=arr[0]
for i in range(1,len(arr)):
    answer-=int(arr[i])


print(answer)