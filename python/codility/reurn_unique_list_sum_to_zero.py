

def solution(N):
    # write your code in Python 3.6
    ret = []
    x = 0
    if 0 != N % 2:
        ret.append(x)
    x += 1
    ret.extend(get_tbl(x, N))
    return ret

def get_tbl(x, N):
    ret = []

    #for i in range(N):
    while len(ret) < N-1:
        ret.append(x)
        ret.append(-1*x)
        x += 1

    return ret


print(solution(6))
print(solution(5))

