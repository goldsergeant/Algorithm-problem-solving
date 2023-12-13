import sys

N = int(sys.stdin.readline())
answer = 0
greater_than_one_nums, one_nums, zero_nums, negative_nums = [], [], [], []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 1:
        greater_than_one_nums.append(num)
    elif num == 1:
        one_nums.append(num)
    elif num == 0:
        zero_nums.append(num)
    else:
        negative_nums.append(num)

greater_than_one_nums.sort(reverse=True)
negative_nums.sort(reverse=True)

for i in range(0, len(greater_than_one_nums) - 1, 2):
    answer += greater_than_one_nums[i] * greater_than_one_nums[i + 1]
if greater_than_one_nums and len(greater_than_one_nums) % 2 == 1:
    answer += greater_than_one_nums[-1]
while len(negative_nums) >= 2:
    a, b = negative_nums.pop(), negative_nums.pop(),
    answer += a * b
while zero_nums and negative_nums:
    zero_nums.pop()
    negative_nums.pop()

answer += sum(one_nums)
answer+= sum(negative_nums)
print(answer)
