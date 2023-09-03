import sys

def get_max_candy(arr):
    dp=[0 for _ in range(len(arr))]
    dp[0]=arr[0]
    if len(arr)>=2:
        dp[1]=max(arr[0],arr[1])

    for i in range(2,len(arr)):
        dp[i]=max(dp[i-1],dp[i-2]+arr[i])

    return dp[-1]

while True:
    m,n=map(int,input().split())
    if m==0 and n==0:
        break
    candies=[]
    for _ in range(m):
        candies.append(list(map(int,sys.stdin.readline().split())))


    arr_row=[]
    for r in candies:
        arr_row.append(get_max_candy(r))

    print(get_max_candy(arr_row))

