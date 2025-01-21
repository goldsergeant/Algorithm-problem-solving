import itertools
import re


def calc(numbers, opts, priority):
    for opt in priority:
        numbers_idx=-1
        for i in range(len(opts)):
            numbers_idx+=1
            if opts[i] != opt:
                continue
            tmp = eval(f'{numbers[numbers_idx]}{opt}{numbers[numbers_idx+1]}')
            numbers[numbers_idx] = tmp
            numbers.pop(numbers_idx+1)
            numbers_idx-=1

        for _ in range(opts.count(opt)):
            opts.remove(opt)

    return abs(numbers[0])


def solution(expression):
    answer = 0
    opts_set = set()
    opts = []
    numbers = re.split('[+|*|-]', expression)
    for ch in expression:
        if not ch.isnumeric():
            opts_set.add(ch)
            opts.append(ch)

    for case in list(itertools.permutations(opts_set, len(opts_set))):
        answer=max(answer,calc(numbers.copy(), opts.copy(), case))
    return answer