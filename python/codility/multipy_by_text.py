

def solution(D, S):
    # write your code in Python 3.6
    s_num = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

    if s_num.get(S):
        return D*s_num[S]
    else :
        return -1


print(solution(2, "five"))
print(solution(2, "err"))

