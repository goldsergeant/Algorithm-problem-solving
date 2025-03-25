from heapq import heappop,heappush

def convert_st_to_int(timezone):
    h,m,s=timezone.split(':')
    return int(h)*3600+int(m)*60+float(s)

def get_start_time_from_end(time,processing_time):
    return time-processing_time+1

def solution(lines):
    answer=0
    for i in range(len(lines)):
        timezone, processing_time = lines[i].split()[1], lines[i].split()[2]
        end_time = int(convert_st_to_int(timezone) * 1000)
        processing_time = processing_time[:-1]
        processing_time = int(float(processing_time) * 1000)
        start_time = get_start_time_from_end(end_time, processing_time) - 1000
        lines[i]=[start_time,end_time]

    for i in range(len(lines)):
        cnt=1
        for j in range(i+1,len(lines)):
            if lines[i][1]>lines[j][0]:
                cnt+=1

        answer=max(answer,cnt)
    return answer

print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))