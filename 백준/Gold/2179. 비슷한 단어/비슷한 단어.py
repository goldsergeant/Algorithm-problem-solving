import sys


def get_common_length(str1, str2):
    cnt = 0
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            break
        cnt += 1
    return cnt


N = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for _ in range(N)]
for i in range(N):
    arr[i] = [arr[i], i]

arr.sort()

max_common_length = 0
s, t = 0, 0
for left in range(N - 1):
    right = left + 1
    while right < N and arr[right][0][0] == arr[left][0][0]:
        if arr[left][0]==arr[right][1]:
            right+=1
            continue
        common = get_common_length(arr[left][0], arr[right][0])
        if max_common_length < common:
            max_common_length = common
            if arr[left][1] < arr[right][1]:
                s, t = left, right
            else:
                s, t = right, left
        elif max_common_length == common:
            if min(arr[s][1], arr[t][1]) > min(arr[left][1], arr[right][1]) or (
                    min(arr[s][1], arr[t][1]) == min(arr[left][1], arr[right][1]) and max(arr[s][1], arr[t][1]) > max(
                    arr[left][1], arr[right][1])):
                if arr[left][1] < arr[right][1]:
                    s, t = left, right
                else:
                    s, t = right, left

        right += 1

print(arr[s][0])
print(arr[t][0])
