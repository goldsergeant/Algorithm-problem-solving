import collections


def solution(n, build_frame):
    def exist_pillar(x, y):
        return (x, y, x, y + 1) in pillars

    def exist_beam(x, y):
        return (x, y, x + 1, y) in beams

    def new_exist_pillar(x, y):
        return (x, y, x, y + 1) in new_pillars
    def new_exist_beam(x, y):
        return (x, y, x+1, y) in new_beams

    def install_pillar(x, y):
        if y == 0 or exist_pillar(x, y - 1) or exist_beam(x - 1, y) or exist_beam(x, y):
            pillars.add((x, y, x, y + 1))

    def install_beam(x, y):
        points = (x, y, x + 1, y)
        if exist_pillar(x, y - 1) or exist_pillar(x + 1, y - 1) or (exist_beam(x - 1, y) and exist_beam(x + 1, y)):
            beams.add(points)

    def can_delete(pillars, beams):  # 지울것만 새거로 넘겨주면 됨
        for x1, y1, x2, y2 in pillars:
            if y1 == 0:
                continue
            if new_exist_pillar(x1, y1 - 1) or new_exist_beam(x1 - 1, y1):
                continue
            if new_exist_beam(x1, y1) or new_exist_beam(x1 - 1, y1):
                continue
            return False
        for x1, y1, x2, y2 in beams:
            if new_exist_pillar(x1,y1-1) or new_exist_pillar(x1+1,y1-1):
                continue
            if new_exist_beam(x1 - 1, y1) and new_exist_beam(x1 + 1, y1):
                continue
            return False
        return True

    # def can_delete_pillar(x, y):
    #     if exist_beam(x - 1, y + 1):  # 위에 왼쪽 보가 있는 경우
    #         if not exist_pillar(x - 1, y) and not (exist_beam(x - 2, y + 1) and exist_beam(x, y + 1)):
    #             return False
    #     if exist_beam(x, y + 1):  # 위에 오른쪽 보가 있는 경우
    #         if not exist_pillar(x + 1, y) and not (exist_beam(x - 1, y + 1) and exist_beam(x + 1, y + 1)):
    #             return False
    #     if exist_pillar(x, y + 1):  # 위에 기둥이 있는 경우
    #         if not (exist_beam(x - 1, y + 1) or exist_beam(x, y + 1)):
    #             return False
    #     return True
    #
    # def can_delete_beam(x, y):
    #     if exist_beam(x - 1, y):  # 왼쪽 보
    #         if not (exist_pillar(x - 1, y - 1) or exist_pillar(x, y - 1)):
    #             return False
    #     if exist_beam(x + 1, y):  # 오른쪽 보
    #         if not (exist_pillar(x + 1, y - 1) or exist_pillar(x + 2, y - 1)):
    #             return False
    #     if exist_pillar(x, y - 1):  # 아래 기둥
    #         if not (exist_beam(x - 1, y - 1) or exist_beam(x, y - 1)) and not (exist_pillar(x, y - 2)):
    #             return False
    #     if exist_pillar(x + 1, y - 1):  # 아래 오른쪽 기둥
    #         if not (exist_beam(x, y - 1) or exist_beam(x + 1, y - 1)) and not (exist_pillar(x + 1, y - 2)):
    #             return False
    #     return True

    def delete_pillar(x, y):
        pillars.remove((x, y, x, y + 1))

    def delete_beam(x, y):
        beams.remove((x, y, x + 1, y))

    answer = []
    pillars = set()
    beams = set()
    new_pillars = set()
    new_beams = set()
    for x, y, a, b in build_frame:
        if a == 0:
            if b == 0:
                new_pillars = pillars.copy()
                new_beams=beams.copy()
                new_pillars.remove((x, y, x, y + 1))
                if can_delete(new_pillars, new_beams):
                    delete_pillar(x, y)
            else:
                install_pillar(x, y)
        else:
            if b == 0:
                new_pillars= pillars.copy()
                new_beams = beams.copy()
                new_beams.remove((x, y, x + 1, y))
                if can_delete(new_pillars, new_beams):
                    delete_beam(x, y)
            else:
                install_beam(x, y)

    for x1, y1, x2, y2 in pillars:
        answer.append([x1, y1, 0])
    for x1, y1, x2, y2 in beams:
        answer.append([x1, y1, 1])

    return sorted(answer)


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
print(solution(5, [[1, 0, 0, 1], [2, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [1, 0, 0, 0]]))
