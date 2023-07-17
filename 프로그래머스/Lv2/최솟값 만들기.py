# 내 풀이
def solution(A,B):
    answer = 0

    for a, b in zip(sorted(A), sorted(B, reverse=True)):
        answer += a * b

    return answer

# 다른 사람 풀이
def solution2(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])

print(solution([1, 4, 2], [5, 4, 4]))
print(solution2([1,2], [3,4]))