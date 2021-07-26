

def solution(N):
    # write your code in Python 3.6
    ret = []

    if 0 != N % 2:
        ret.append(0)

    ret.extend(get_tbl(1, N))
    return ret


def get_tbl(x, N):
    ret = []

    while len(ret) < N-x:
        ret.append(x)
        ret.append(-1 * x)
        x += 1

    return ret


print(solution(6))
print(solution(5))

