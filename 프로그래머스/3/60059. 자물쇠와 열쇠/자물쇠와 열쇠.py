import copy


def solution(key, lock):
    def get_rotate_right_key(key):
        new_key = [[0 for _ in range(len(key))] for _ in range(len(key))]
        for i in range(len(key)):
            for j in range(len(key)):
                new_key[j][len(key) - 1 - i] = key[i][j]

        return new_key

    def get_rotate_right_lock(lock):
        new_lock = [[0 for _ in range(len(lock))] for _ in range(len(lock))]
        for i in range(len(lock)):
            for j in range(len(lock)):
                new_lock[j][len(lock) - 1 - i] = lock[i][j]

        return new_lock

    def check_key(key_in_lock_s_r, key_in_lock_s_c):
        for i in range(len(lock)):
            for j in range(len(lock)):
                key_i = i - key_in_lock_s_r
                key_j = j - key_in_lock_s_c

                if 0 <= key_i < len(key) and 0 <= key_j < len(key):
                    if key[key_i][key_j] == lock[i][j] or max(key[key_i][key_j], lock[i][j]) == 0:
                        return False
                else:
                    if lock[i][j] == 0:
                        return False

        return True

    # lock = get_rotate_right_lock(lock)
    # lock = get_rotate_right_lock(lock)
    # print(check_key(0, 2))

    for _ in range(4):
        key = get_rotate_right_key(key)
        for _ in range(4):
            lock = get_rotate_right_lock(lock)
            for lock_s_r in range(len(lock)):
                for lock_s_c in range(len(lock)):
                    if check_key(lock_s_r, lock_s_c):
                        return True

    return False