

def solution(s):
    d = {}
    s_list = s.split(',')

    for i, num in enumerate(s_list):
        if num not in d:
            d[num] = 1
        else:
            d[num] += 1

    return d


s = '6,2,4,4,4,2,5,6,7,10,2,2,6,7,8,8,8,8'
print(solution(s))
