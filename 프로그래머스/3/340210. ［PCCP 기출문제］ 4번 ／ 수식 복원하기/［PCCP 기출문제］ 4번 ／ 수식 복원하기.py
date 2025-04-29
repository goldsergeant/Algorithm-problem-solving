def solution(expressions):
    def ten_to_n(ten_num,base):
        tmp=[]
        while ten_num:
            a,b=divmod(ten_num,base)
            tmp.append(b)
            ten_num//=base
            
        return ''.join(map(str,tmp[::-1])) if tmp else '0'
    
    def sure_check(exp):
        a,b,c=exp.replace('+','').replace('=','').replace('-','').split()
        opt=''
        if '-' in exp:
            opt='-'
        elif '+' in exp:
            opt='+'
            
        for base in range(2,9+1):
            flag=True
            for ch in a+b+c:
                if int(ch)>=base:
                    possible_base[base]=False
                    flag=False
                    break
                    
            if not flag:
                continue
                
            if opt=='-':
                if int(a,base)-int(b,base)!=int(c,base):
                    possible_base[base]=False
            elif opt=='+':
                if int(a,base)+int(b,base)!=int(c,base):
                    possible_base[base]=False
    
    def not_sure_check(exp):
        a,b,c=exp.replace('+','').replace('=','').replace('-','').split()
        for base in range(2,9+1):
            for ch in a+b:
                if int(ch)>=base:
                    possible_base[base]=False
                    break
                    
    def get_answer(exp):
        possible_c=set()
        for base in range(2,9+1):
            if not possible_base[base]:
                continue
            a,b,c=exp.replace('+','').replace('=','').replace('-','').split()
            opt=''
            if '-' in exp:
                opt='-'
            elif '+' in exp:
                opt='+'
            
            if opt=='-':
                possible_c.add(ten_to_n(int(a,base)-int(b,base),base))
            elif opt=='+':
                possible_c.add(ten_to_n(int(a,base)+int(b,base),base))
        
        if len(possible_c)>1:
            answer.append(f'{a} {opt} {b} = ?')
        else:
            answer.append(f'{a} {opt} {b} = {list(possible_c)[0]}')
        
                    
    answer = []
    possible_base=[True for _ in range(9+1)]
    sure_exps=[]
    not_sure_exps=[]
    for exp in expressions:
        if exp[-1]=='X':
            not_sure_exps.append(exp)
        else:
            sure_exps.append(exp)
            
    for exp in sure_exps:
        sure_check(exp)
        
    for exp in not_sure_exps:
        not_sure_check(exp)
    
    print(possible_base)
    for exp in not_sure_exps:
        get_answer(exp)
    return answer