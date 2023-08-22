from math import ceil

one = int(input())
two = int(input())
three = int(input())
four = int(input())
five = int(input())
six = int(input())


def get_paper_by234(two, three, four):
    two = max(0, two - 5 * four)
    three_need_cnt = 0 if three % 4 == 0 else 4 - three % 4
    two = max(0, two - [0, 1, 3, 5][three_need_cnt])
    return four + ceil(three / 4) + ceil(two / 9)


paper = six + five + get_paper_by234(two, three, four)
remain_area = 36 * paper - 36 * six - 25*five - 16*four - 9 *three - 4 * two
one = max(0,one-remain_area)
print(paper+ceil(one/36))