n=int(input())
for _ in range(n):
    arr=map(int,input().split())
    print(sorted(arr)[-3])