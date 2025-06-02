def solution(dirs):
    answer = 0
    first_road_set=set()
    
    cur_r,cur_c=0,0
    
    for command in dirs:
        prev_r,prev_c=cur_r,cur_c
        if command=='U':
            if cur_r<5:
                prev_r=cur_r
                cur_r+=1
        elif command=='D':
            if cur_r>-5:
                prev_r=cur_r
                cur_r-=1
        elif command=='R':
            if cur_c<5:
                prev_c=cur_c
                cur_c+=1
        elif command=='L':
            if cur_c>-5:
                prev_c=cur_c
                cur_c-=1
        if (prev_r,prev_c) != (cur_r,cur_c):
            first_road_set.add(tuple(sorted([(prev_r,prev_c),(cur_r,cur_c)])))
    return len(first_road_set)