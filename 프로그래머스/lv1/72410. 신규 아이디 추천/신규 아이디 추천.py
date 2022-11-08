def solution(new_id):
    new_id=new_id.lower() #1단계
    
    for char in new_id: #2단계
        if not char.isdigit() and char!='-' and char!='_' and char!='.' and not char.isalpha():
            new_id=new_id.replace(char,'')
    
    while '..' in new_id:
        new_id=new_id.replace('..','.')
    
    new_id=new_id.strip('.')
    
    if new_id=='':
        new_id='a'
    
    if len(new_id)>=16:
        new_id=new_id[:15].strip('.')
    if len(new_id)<=2:
        while len(new_id)<3:
            new_id=new_id+new_id[-1]
    
    return new_id
        