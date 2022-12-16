n = int(input())
arr = list(map(int, input().split()))
opt = list(map(int, input().split()))
answer = []


def dfs(result, index):
    if index >= len(arr)-1:
        answer.append(result)
        return
    for i in range(len(opt)):
        if i == 0 and opt[i] > 0:
            opt[i] -= 1
            dfs(result + arr[index + 1], index + 1)
            opt[i] += 1
        elif i == 1 and opt[i] > 0:
            opt[i] -= 1
            dfs(result - arr[index + 1], index + 1)
            opt[i] += 1
        elif i == 2 and opt[i] > 0:
            opt[i] -= 1
            dfs(result * arr[index + 1], index + 1)
            opt[i] += 1
        elif i == 3 and opt[i] > 0:
            opt[i] -= 1
            if result<0:
                dfs(-(-result//arr[index+1]),index+1)
            else:
                dfs(result // arr[index + 1], index + 1)
            opt[i] += 1


dfs(arr[0], 0)
print(max(answer))
print(min(answer))
