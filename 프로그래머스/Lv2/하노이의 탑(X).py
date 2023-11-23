# 다른 사람 풀이
def solution(n):
    def hanoi(num, start, end):
    	# 1개짜리 탑 즉 가장 작은 원판은 그냥 목표지점으로 옮기면 된다
        if num == 1:
            return [[start, end]]
        # 그게 아니라면, 출발/도착이 아닌 another의 위치를 알아야 한다.
        another = 0
        for i in range(1,4):
            if i != start and i != end:
                another = i
                break
        # n-1개짜리 탑을 다른 지점에 옮기고, n번째 원판을 목표지점에 옮기고, n-1개를 목표 지점으로 옮기면 된다!
        return hanoi(num-1, start, another) + [[start, end]] + hanoi(num-1, another, end)
    # n개짜리 탑을, 1번 지점에서 3번지점으로 옮기는 call을 하면 끝
    return hanoi(n, 1, 3)

print(solution(2))
print(solution(3))