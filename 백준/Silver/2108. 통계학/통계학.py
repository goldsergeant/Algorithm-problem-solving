import collections

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

arr.sort()
counter=collections.Counter(arr)
most=counter.most_common(1)[0][1]
print(round(sum(arr)/len(arr)))
print(arr[len(arr)//2])
temp=[]
for i in counter.keys():
    if counter[i]==most:
        temp.append(i)

print(temp[0] if len(temp)==1 else temp[1])
print(max(arr)-min(arr))
