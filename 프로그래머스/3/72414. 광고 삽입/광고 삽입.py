import sys


def time_str_to_int(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_time_str(time_int):
    h = time_int // 3600
    m = (time_int % 3600) // 60
    s = time_int % 60

    h_st = str(h).zfill(2)
    m_st = str(m).zfill(2)
    s_st = str(s).zfill(2)

    return f'{h_st}:{m_st}:{s_st}'


def solution(play_time, adv_time, logs):
    answer_int = sys.maxsize
    play_time_int = time_str_to_int(play_time)
    adv_time_int = time_str_to_int(adv_time)
    start_time_arr = []
    imos = [0 for _ in range(play_time_int + 2)]
    t_sum = [0 for _ in range(play_time_int + 2)]

    for st in logs:
        start_time, end_time = st.split('-')
        start_int = time_str_to_int(start_time)
        end_int = time_str_to_int(end_time)
        imos[start_int] += 1
        imos[end_int] -= 1

        start_time_arr.append(start_int)

    for i in range(1, play_time_int + 1):
        imos[i] += imos[i - 1]

    t_sum[0]=imos[0]
    for i in range(1, play_time_int + 1):
        t_sum[i] += t_sum[i - 1] + imos[i]

    max_duration = 0
    for start_int in range(play_time_int - adv_time_int + 1):
        cur_duration = t_sum[start_int + adv_time_int-1] - t_sum[max(0,start_int - 1)]
        if cur_duration > max_duration:
            answer_int = start_int
            max_duration = cur_duration
        elif cur_duration == max_duration:
            if start_int < answer_int:
                answer_int = start_int

    return int_to_time_str(answer_int)


print(solution("02:03:55", "00:14:15",
               ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00",
               ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))

print(time_str_to_int('99:59:59'))
print(int_to_time_str(359999))
