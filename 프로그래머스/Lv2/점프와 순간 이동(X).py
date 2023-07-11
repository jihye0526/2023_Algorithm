# 다른 사람 풀이 1
def solution(N):
    answer = 0
    while N > 0:
        answer += N % 2
        N //= 2
    return answer

# 다른 사람 풀이 2
# 2의 제곱이면 처음 0 -> 1 빼고 순간이동으로 갈 수 있다. 이를 이진수로 표현해 보면 1이 하나인 이진수
# 즉, 건전지 사용량은 이진수로 변환했을 때 1의 개수와 같음
def solution2(N):
    return bin(N).count('1')

print(solution(5))
print(solution(6))
print(solution2(5000))