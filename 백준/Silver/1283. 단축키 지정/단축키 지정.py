import collections
import sys

is_shortkey=collections.defaultdict(bool)
N=int(sys.stdin.readline())
for _ in range(N):
    st=sys.stdin.readline().rstrip()
    words=st.split()
    check_idx=0
    flag=False
    for word in words:
        if not is_shortkey[word[0].lower()]:
            is_shortkey[word[0].lower()] = True
            flag=True
            break
        check_idx+=len(word)+1

    if not flag:
        for i in range(len(st)):
            if st[i].isspace():
                continue
            if not is_shortkey[st[i].lower()]:
                flag=True
                is_shortkey[st[i].lower()] = True
                check_idx=i
                break

    if flag:
        print(st[:check_idx]+'['+st[check_idx]+']'+st[check_idx+1:])
    else:
        print(st)