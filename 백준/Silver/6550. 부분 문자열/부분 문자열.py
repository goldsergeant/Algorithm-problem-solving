while True:
    try:
        s,t=input().split()
        if s=='' or t=='':
            break
    
        idx=0
        for char in t:
            if idx<len(s) and char==s[idx]:
                idx+=1
    
        print('Yes' if idx==len(s) else 'No')
    except EOFError:
        break