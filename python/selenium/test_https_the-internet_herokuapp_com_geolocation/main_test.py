
import unittest

import TestSet_PAGE_LAYOUT
import TestSet_OPEARATING_MODE
import TestSet_FAILURES_HANDLING
import TestSet_PERFORMANCE

import random
"""
    # PAGE LAYOUT
        # Test_Scenario_1 testPageTitle
        # Test_Scenario_2 testPageTitleAfterScriptRun

    # OPEARATING MODE
        # Test_Scenario_1 testCheckGeo
        # Test_Scenario_2 testCheckGeoUpdate
        # Test_Scenario_3 testNegativeCoordinates
        # Test_Scenario_4 testBoundaryCoordinates
        # Test_Scenario_5 testCheckGoogleMapsLink
        # Test_Scenario_6 testCheckGoogleMapsLinkUpdate

    # FAILURES HANDLING
        # Test_Scenario_1 testOffGlobeCoordinates

    # PERFORMANCE
        # Test_Scenario_1 testTimings
        # Test_Scenario_2 testResponseUnderLoad


suite = []

suite.append(unittest.TestLoader().loadTestsFromModule(TestSet_PAGE_LAYOUT))
suite.append(unittest.TestLoader().loadTestsFromModule(TestSet_OPEARATING_MODE))
#suite.append(unittest.TestLoader().loadTestsFromModule(TestSet_FAILURES_HANDLING))
suite.append(unittest.TestLoader().loadTestsFromModule(TestSet_PERFORMANCE))

for st in suite:
    unittest.TextTestRunner(verbosity=2).run(st)




# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    return rec(1, A)


def rec(r, A):
    for a in A:
        if a == r:
            r = rec(r+1, A)
            break
    return r

"""
"""
def solution(X, Y, A):
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

A = []
for i in range(20):
    A.append(random.randint(0, 10))

print(A)
print(solution(1, 1, A))
"""

"""
def solution(A):
    ans = 0
    for i in range(0, len(A)):
        ans = ans + A[i]
    return ans
"""

"""
def solution(D, S):
    # write your code in Python 3.6
    s_num = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

    if s_num.get(S):
        return D*s_num[S]
    else :
        return -1

"""
"""
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
"""

def solution(N):
    # write your code in Python 3.6
    num_lst = []
    n = str(N)

    for i,d in enumerate(n):

        if d.isdigit():
            num_lst.append(int(n[:i] + '5' + n[i:]))
        else:
            continue

   # num_lst.append(int(n[:0] + '5' + n[0:]))
    #num_lst.append(int(n[:1] + '5' + n[1:]))
    #num_lst.append(int(n[:2] + '5' + n[2:]))
    #num_lst.append(int(n[:3] + '5' + n[3:]))

    return max(num_lst)



#print(solution([-1,2,3]))
#print(solution(2,'x'))
#print(solution(5))
#print(solution(6))

print(solution(-25))