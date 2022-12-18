a, b = map(int, input().split())

def factor():
    result = 1
    for i in range(2, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            if i > result:
                result = i
    return result


def multiple():
    result = 0
    i = max(a, b)
    while True:
        if i % a == 0 and i % b == 0:
            result = i
            break
        i+=1
    return result


print(factor())
print(multiple())
