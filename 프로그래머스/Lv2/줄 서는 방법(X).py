# 다른 사람 풀이
from math import factorial

def solution(n, k):
    answer = []
    order = list(range(1,n+1))
    while n!=0 :
        fact = factorial(n-1)
        answer.append(order.pop((k-1)//fact))
        n,k = n-1, k%fact
    return answer

def solution2(n, k):
    answer = []
    arr = [i for i in range(1, n+1)]

    while n != 0:
        cnt = fact(n-1)
        fix = k // cnt
        k = k % cnt

        if k == 0:
            answer.append(arr.pop(fix-1))
        else:
            answer.append(arr.pop(fix))
        n -= 1

    return answer

def fact(n):
    if n <= 1: return 1

    return n * fact(n-1)

print(solution(3, 5))
print(solution2(3, 5))