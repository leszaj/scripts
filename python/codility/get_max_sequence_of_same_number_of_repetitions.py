
import random

def solution(X, Y, A):
    # write your code in Python 3.6
    N = len(A)
    result = -1
    nX = 0
    nY = 0

    for i in range(N):
        if A[i] == X:
            nX += 1
        elif A[i] == Y:
            nY += 1
        if (0 != nX) and (nX == nY):
            result = i

    return result


test = []
for i in range(20):
    test.append(random.randint(0, 10))


print(test)
print(solution(1, 1, test))

