# 내 풀이
def solution(n):
    answer = ['수' if i % 2 == 0 else '박' for i in range(n)]
    return ''.join(answer)

# 다른 사람 풀이
def solution2(n):
    str = "수박"*n
    return str[:n]

print(solution(3))
print(solution2(4))