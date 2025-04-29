def time_to_int(time):
    h,m=time.split(':')
    return 60*int(h)+int(m)

def int_to_time(num):
    h=num//60
    m=num%60
    return f'{str(h).zfill(2)}:{str(m).zfill(2)}'

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len,pos,op_start,op_end=time_to_int(video_len),time_to_int(pos),time_to_int(op_start),time_to_int(op_end)
    
    cur=op_end if op_start<=pos<=op_end else pos
    
    for query in commands:
        if query=='prev':
            cur=max(cur-10,0)
        elif query=='next':
            cur=min(cur+10,video_len)
        if op_start<=cur<=op_end:
            cur=op_end
            
    return int_to_time(cur)