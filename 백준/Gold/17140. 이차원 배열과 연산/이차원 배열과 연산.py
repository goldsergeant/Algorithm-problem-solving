import collections
import sys

r,c,k=map(int,sys.stdin.readline().split())
r-=1
c-=1
a_arr=[]
second=0
for _ in range(3):
    a_arr.append(list(map(int,sys.stdin.readline().split())))

while True:
    if (r<len(a_arr) and c<len(a_arr[r]) and a_arr[r][c]==k) or second>100:
        break

    if len(a_arr[0])<= len(a_arr): # R 연산
        max_len=0
        for row in range(len(a_arr)):
            counter=collections.Counter(filter(lambda x:x!=0,a_arr[row]))
            tmp=[]
            for key in sorted(counter.keys(),key=lambda x:(counter[x],x)):
                tmp.append(key)
                tmp.append(counter[key])
            a_arr[row]=tmp[:100]
            max_len=max(max_len,len(a_arr[row]))

        for row in range(len(a_arr)):
            a_arr[row]+=[0 for _ in range(max_len-len(a_arr[row]))]

    elif len(a_arr[0])>len(a_arr): # C 연산
        tmp=[]
        max_len=0
        for col in range(len(a_arr[0])):
            vertical_arr=[]
            for row in range(len(a_arr)):
                if a_arr[row][col]!=0:
                    vertical_arr.append(a_arr[row][col])
            counter=collections.Counter(vertical_arr)
            tmp2=[]
            for key in sorted(counter.keys(),key=lambda x:(counter[x],x)):
                tmp2.append(key)
                tmp2.append(counter[key])
            tmp.append(tmp2[:100])
            max_len=max(max_len,len(tmp2[:100]))
        for row in range(len(tmp)):
            tmp[row]+=[0 for _ in range(max_len-len(tmp[row]))]

        a_arr=[]
        for col in range(len(tmp[0])):
            tmp3=[]
            for row in range(len(tmp)):
                tmp3.append(tmp[row][col])
            a_arr.append(tmp3)

    second+=1

print(second if second<=100 else -1)




