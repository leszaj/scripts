
import random

def solution(A):
    # write your code in Python 3.6
    return rec(1, A)


def rec(r, A):
    for a in A:
        if a == r:
            r = rec(r+1, A)
            break
    return r


test = []
for i in range(10):
    test.append(random.randint(0, 10))


print(test)
print(solution(test))

