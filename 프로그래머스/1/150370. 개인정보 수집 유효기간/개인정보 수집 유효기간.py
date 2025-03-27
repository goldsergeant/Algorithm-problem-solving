def convert_time_to_int(time):
    y,m,d=time.split('.')
    return int(y)*(28*12)+(int(m)-1)*28+int(d)

def solution(today, terms, privacies):
    answer = []
    valid_dates=dict()
    today_int=convert_time_to_int(today)
    for term in terms:
        what,month=term.split()
        valid_dates[what]=28*int(month)
    
    for i,privacy in enumerate(privacies):
        time,what=privacy.split()
        print(convert_time_to_int(time),today_int,valid_dates[what])
        if convert_time_to_int(time)<=today_int-valid_dates[what]:
            answer.append(i+1)
    
    print(valid_dates)
    return answer