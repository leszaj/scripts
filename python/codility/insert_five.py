

def solution(N):
    # write your code in Python 3.6
    num_lst = []
    n = str(N)

    for i,d in enumerate(n):

        if d.isdigit():
            num_lst.append(int(n[:i] + '5' + n[i:]))
        else:
            continue

    num_lst.append(int(n + '5'))

    #num_lst.append(int(n[:0] + '5' + n[0:]))
    #num_lst.append(int(n[:1] + '5' + n[1:]))
    #num_lst.append(int(n[:2] + '5' + n[2:]))
    #num_lst.append(int(n[:3] + '5' + n[3:]))

    print(num_lst)
    return max(num_lst)


print(solution(6))
print(solution(6232))
print(solution(0))
print(solution(-25))

