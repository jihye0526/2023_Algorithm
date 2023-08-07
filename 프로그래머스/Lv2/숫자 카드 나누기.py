# 다른 사람 풀이 1
from math import gcd
from functools import reduce

def check(arrayA, arrayB):
    gcd_A = reduce(gcd, arrayA, arrayA[0])
    factors = [i for i in range(1, gcd_A//2+1) if not gcd_A % i]
    factors.append(gcd_A)
    for factor in factors[::-1]:
        if all(i % factor for i in arrayB):
            return gcd_A
    return 0

def solution(arrayA, arrayB):
    return max(check(arrayA, arrayB), check(arrayB, arrayA))

# 다른 사람 풀이 2
def solution2(nums1, nums2):
    gcd1, gcd2 = reduce(gcd, nums1), reduce(gcd, nums2)
    answer = []
    if all(each % gcd2 for each in nums1):
        answer.append(gcd2)
    if all(each % gcd1 for each in nums2):
        answer.append(gcd1)
    return max(answer) if answer else 0

print(solution([10, 17], [5, 20]))
print(solution2([10, 20], [5, 17]))
print(solution2([14, 35, 119], [18, 30, 102]))