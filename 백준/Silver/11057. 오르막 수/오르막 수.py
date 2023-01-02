n=int(input())
stairs=[[0 for i in range(10)] for i in range(n+1)]
stairs[1]=[1 for i in range(10)]

for i in range(1,n+1):
    stairs[i][0]=1

for i in range(2,n+1):
    for j in range(1,10):
        stairs[i][j]=stairs[i][j-1]+stairs[i-1][j]

print(sum(stairs[n])%10007)