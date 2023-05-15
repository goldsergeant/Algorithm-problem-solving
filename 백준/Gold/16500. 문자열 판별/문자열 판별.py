S=input()
N=int(input())
words=[]
dp=[0 for _ in range(len(S)+1)]
for _ in range(N):
    words.append(input())

def search(idx):
    if idx==len(S):
        dp[idx]=1
        return

    if dp[idx]!=1:
        dp[idx]=1

        for i in range(N):
            if len(S[idx:])>=len(words[i]) and S[idx:idx+len(words[i])]==words[i]:
                search(idx+len(words[i]))


search(0)
print(dp[len(S)])