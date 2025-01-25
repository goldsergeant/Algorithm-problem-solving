import collections
import math


def convert_time_to_int(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)


def solution(fees, records):
    car_time = collections.defaultdict(int)
    car_in_dict = dict()
    answer=[]
    for st in records:
        time, num, query = st.split()
        if query == 'IN':
            car_in_dict[num] = convert_time_to_int(time)
        else:
            car_time[num] += convert_time_to_int(time) - car_in_dict[num]
            car_in_dict.pop(num)

    for key, val in car_in_dict.items():
        car_time[key] += convert_time_to_int('23:59') - val

    for key in sorted(car_time.keys()):
        how_many = car_time[key]
        if how_many<fees[0]:
            answer.append(fees[1])
        else:
            default_money=fees[1]
            additional_money=math.ceil((how_many-fees[0])/fees[2])*fees[3]
            answer.append(default_money+additional_money)
    return answer