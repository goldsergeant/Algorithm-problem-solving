def solution(record):
    answer = []
    uid_nickname=dict()
    for string in record:
        query=string.split()[0]
        if query=='Enter':
            uid,nickname=string.split()[1:]
            uid_nickname[uid]=nickname
        elif query=='Change':
            uid,nickname=string.split()[1:]
            uid_nickname[uid]=nickname

    for string in record:
        query = string.split()[0]
        if query == 'Enter':
            uid, nickname = string.split()[1:]
            answer.append(f'{uid_nickname[uid]}님이 들어왔습니다.')
        elif query=='Leave':
            uid=string.split()[1]
            answer.append(f'{uid_nickname[uid]}님이 나갔습니다.')
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))