from bisect import bisect_right


def convert_str_to_time(time_str):
    h, m = time_str.split(':')
    return int(h) * 60 + int(m)


def convert_time_to_str(time):
    h = time // 60
    m = time % 60
    return f'{str(h).zfill(2)}:{str(m).zfill(2)}'


def solution(n, t, m, timetable):
    def check(val):
        tmp_time_table = timetable[::]
        target_idx = bisect_right(tmp_time_table, val)
        tmp_time_table.insert(target_idx, val)
        idx = 0
        shuttle_cnt = 0
        cur_people = 0
        cur_shuttle_time = 540
        while shuttle_cnt < n:
            while idx < len(tmp_time_table) and tmp_time_table[idx] <= cur_shuttle_time and cur_people < m:
                idx += 1
                cur_people += 1
            shuttle_cnt += 1
            cur_people = 0
            cur_shuttle_time += t

        return target_idx < idx

    timetable = sorted(list(map(convert_str_to_time, timetable)))

    left = min(540,min(timetable)) - 1
    right = 1439 # 23:59

    while left + 1 < right:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid

    return convert_time_to_str(left)