def solution(arr):
    global array
    array = arr

    def dfs(left, right, top, bottom):
        if left == right:
            if array[top][left] == 1:
                return [0, 1]
            else:
                return [1, 0]

        vertical_mid = (top + bottom) // 2
        horizontal_mid = (left + right) // 2
        l_t = dfs(left, horizontal_mid, top, vertical_mid)
        r_t = dfs(horizontal_mid + 1, right, top, vertical_mid)
        l_b = dfs(left, horizontal_mid, vertical_mid + 1, bottom)
        r_b = dfs(horizontal_mid + 1, right, vertical_mid + 1, bottom)
        arr = [l_t, r_t, l_b, r_b]
        if all((i[0]==1 and i[1]==0) for i in arr):
            return [1, 0]
        if all((i[0]==0 and i[1]==1) for i in arr):
            return [0, 1]

        tmp=[0,0]
        for zero,one in arr:
           tmp[0]+=zero
           tmp[1]+=one
        return tmp
    answer = []
    return dfs(0, len(arr) - 1, 0, len(arr) - 1)


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))
