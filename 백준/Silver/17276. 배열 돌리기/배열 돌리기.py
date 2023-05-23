import sys

T=int(input())

dy=[-1,-1,0,1,1,1,0,-1]
dx=[0,1,1,1,0,-1-1-1]

def turn45(n,d,arr):
    reps=abs(d)//45
    for _ in range(reps):
        pre_list = []
        if d>0:
            for i in range(n): # 왼쪽으로 누운 대각선
                pre_list.append(arr[i][i])
            for i in range(n): # 왼쪽으로 누운 대각선 -> 가운데 세로
                arr[i][n//2],pre_list[i]=pre_list[i],arr[i][n//2]
            for i in range(n): # 가운데 세로 -> 오른쪽으로 누운 대각선
                arr[i][n-i-1],pre_list[i]=pre_list[i],arr[i][n-i-1]
            for i in range(n): # 오른쪽으로 누운 대각선 -> 가운데 가로
                arr[n//2][n-i-1],pre_list[i]=pre_list[i],arr[n//2][n-i-1]
            for i in range(n): # 가운데 가로 -> 왼쪽으로 누운 대각선
                arr[n-i-1][n-i-1],pre_list[i]=pre_list[i],arr[n-i-1][n-i-1]

        else:
            for i in range(n): # 오른쪽으로 누운 대각선
                pre_list.append(arr[i][n-i-1])
            for i in range(n): # 오른쪽으로 누운 대각선 -> 가운데 세로
                arr[i][n//2],pre_list[i]=pre_list[i],arr[i][n//2]
            for i in range(n): # 가운데 세로 -> 왼쪽으로 누운 대각선
                arr[i][i],pre_list[i]=pre_list[i],arr[i][i]
            for i in range(n): # 왼쪽으로 누운 대각선 -> 가운데 가로
                arr[n//2][i],pre_list[i]=pre_list[i],arr[n//2][i]
            for i in range(n): # 가운데 가로 -> 오른쪽으로 누운 대각선
                arr[n-i-1][i],pre_list[i]=pre_list[i],arr[n-i-1][i]


for _ in range(T):
    n,d=map(int,sys.stdin.readline().split())
    arr=[]
    for _ in range(n):
        arr.append(list(map(int,sys.stdin.readline().split())))

    turn45(n,d,arr)

    for i in arr:
        for j in i:
            print(j,end=' ')
        print()


