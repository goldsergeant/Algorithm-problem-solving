def solution(numbers):
    global flag

    def preorder(left,right):
        global flag
        if flag and left<right:
            mid = (left+right)//2
            if binary[mid] == '0' and '1' in binary[left:right+1]:
                flag = False
            else:
                preorder(left,mid-1)
                preorder(mid+1,right)

    answer = []
    for num in numbers:
        flag = True
        binary = bin(num)[2:]
        target_len = 1
        while len(binary) >= target_len:
            target_len *= 2

        binary = binary.zfill(target_len - 1)
        preorder(0,target_len-1)
        answer.append(1 if flag else 0)

    return answer