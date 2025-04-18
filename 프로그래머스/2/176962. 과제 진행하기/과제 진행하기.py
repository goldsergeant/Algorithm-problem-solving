import sys


def convert_time_to_int(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)


def solution(plans):
    answer = []
    ing_homeworks = []
    plans = sorted(map(lambda x: [x[0], convert_time_to_int(x[1]), int(x[2])], plans), key=lambda x: x[1])
    plans.append(['nothing', sys.maxsize, sys.maxsize])
    for i in range(len(plans) - 1):
        if plans[i][1] + plans[i][2] <= plans[i + 1][1]:
            answer.append(plans[i][0])
            end_t = plans[i][1] + plans[i][2]
            while ing_homeworks:
                h, s_t, d = ing_homeworks.pop()
                end_t += d
                if end_t > plans[i + 1][1]:
                    ing_homeworks.append([h, s_t, end_t-plans[i+1][1]])
                    break

                answer.append(h)
        else:
            ing_homeworks.append([plans[i][0],plans[i][1],plans[i][1]+plans[i][2]-plans[i+1][1]])
    return answer