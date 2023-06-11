import sys

k=int(sys.stdin.readline().rstrip())
size=1
while size<k:
    size=size<<1

size_answer=size
count=0
while k > 0:
    if k >= size:
        k -= size
    else:
        size //= 2
        count += 1
print(f'{size_answer} {count}')
