while True:
    n=int(input())
    if n==0:
        break

    words=[]
    for _ in range(n):
        words.append(input())

    print(sorted(words,key=lambda x:x.lower())[0])

