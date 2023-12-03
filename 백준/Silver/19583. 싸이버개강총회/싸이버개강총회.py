import collections
import sys

s, e, q = sys.stdin.readline().split()
dic = collections.defaultdict(list)
answer = 0
while True:
    st = sys.stdin.readline().rstrip()
    if st == '':
        break

    time, person = st.split()
    dic[person].append(time)

for key, arr in dic.items():
    is_in, is_out = False, False
    for time in arr:
        if time <= s:
            is_in=True
        elif e<=time<=q:
            is_out=True

    if is_in and is_out:
        answer+=1
print(answer)