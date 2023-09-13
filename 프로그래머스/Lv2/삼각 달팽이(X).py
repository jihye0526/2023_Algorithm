# 다른 사람 풀이 1
def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)] # 삼각형 구조 만들기
 
    x, y = -1, 0 # 좌표 초기화 => 처음 시작은 아래로 내려가기 때문에 x = -1
    num = 1
 
    for i in range(n): # 방향
        for j in range(i, n): # 좌표 구하기
            if i % 3 == 0: # 하
                x += 1
            elif i % 3 == 1: # 우
                y += 1
            else: # 상
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
 
    return sum(answer, []) #  2차원 배열를 sum(arr, [])를 통해 1차원 배열로 변환

print(solution(4))
print(solution(5))
print(solution(6))