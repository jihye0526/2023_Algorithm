# 내 풀이
def solution(k, m, score):
    answer = 0

    score.sort(reverse=True)
    cnt = len(score) // m

    for i in range(1, cnt+1):
        answer += score[i*m-1] * m

    return answer

# 다른 사람 풀이
def solution2(k, m, score):
    return sum(sorted(score)[len(score)%m::m]) * m # len(score)%m 부터 끝까지 m 간격으로 배열을 만듦

print(solution2(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution2(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))