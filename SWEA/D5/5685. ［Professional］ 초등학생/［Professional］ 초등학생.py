mod_num=1234567891
def dfs(idx,total):
    global answer
    if idx==N-2:
        if total==target:
            return 1
        return 0
    if dp[idx][total]!=-1:
        return dp[idx][total]

    dp[idx][total]=0
    if 0<=total+numbers[idx+1]<=20:
        dp[idx][total]=(dp[idx][total]+dfs(idx+1,total+numbers[idx+1]))%mod_num
    if 0<=total-numbers[idx+1]<=20:
        dp[idx][total]=(dp[idx][total]+dfs(idx+1,total-numbers[idx+1]))%mod_num
    return dp[idx][total]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    numbers=list(map(int,input().split()))
    numbers,target=numbers[:len(numbers)-1],numbers[-1]
    dp=[[-1 for _ in range(20+1)] for _ in range(N+1)]
    print(f'#{test_case} {dfs(0,numbers[0])}')