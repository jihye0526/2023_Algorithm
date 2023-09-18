# 다른 사람 풀이
def solution(queue1, queue2):
    target = (sum(queue1) + sum(queue2)) // 2
    cur = sum(queue1)
    queue3 = queue1 + queue2 + queue1

    s = 0
    e = len(queue1) - 1
    answer = 0
    while True:
        if cur == target:
            return answer
        if cur < target:
            e += 1
            if e >= len(queue3):
                return -1
            cur += queue3[e]
        else:
            cur -= queue3[s]
            s += 1
        answer += 1

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))