import sys

n = int(input())
s = set()
for _ in range(n):
    st = sys.stdin.readline().strip().split()

    if st[0] == 'all':
        s = set([i for i in range(1, 21)])
    elif st[0] == 'empty':
        s = set()
    else:
        command, x = st[0],st[1]
        x = int(x)
        if command == 'add':
            s.add(x)
        elif command == 'remove':
            s.discard(x)
        elif command == 'check':
            print(1 if x in s else 0)
        elif command == 'toggle':
            if x in s:
                s.remove(x)
            else:
                s.add(x)
