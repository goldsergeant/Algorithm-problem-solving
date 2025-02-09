def solution(numbers):
    global is_possible
    answer = []
    is_possible = True
    tree_length = [1]
    factor = 2
    while tree_length[-1] <= 10000:
        tree_length.append(tree_length[-1] + factor)
        factor *= 2

    for i in range(len(numbers)):
        l = len(bin(numbers[i])[2:])
        numbers[i] = bin(numbers[i])[2:]
        for j in range(1, len(tree_length)):
            if tree_length[j - 1] < l <= tree_length[j]:
                l = tree_length[j]
                numbers[i] = numbers[i].zfill(l)
                break

    def preorder(num, left, right):
        global is_possible
        if left == right:
            return num[left]

        mid = (left + right) // 2
        l = preorder(num, left, mid - 1)
        r = preorder(num, mid + 1, right)
        if num[mid] == '0':
            if l=='1' or r=='1':
                is_possible = False

        return num[mid]

    for num in numbers:
        is_possible = True
        preorder(num, 0, len(num) - 1)
        answer.append(int(is_possible))
    return answer