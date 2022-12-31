n = int(input())
pattern = input()
f, l = pattern.split('*')
for _ in range(n):
    st = input()
    if st.startswith(f):
        if st[len(f):].endswith(l):
            print("DA")
            continue
    print("NE")
