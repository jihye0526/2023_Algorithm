# 내 풀이(시간 초과)
def solution(n, left, right):
    answer = []
    arr = [[0] * n for _ in range(n)]
    
    for i in range(n):
        x, y = i, i
        arr[x][y] = i+1
        
        while x > 0:
            x -= 1
            y -= 1
            arr[x][i] = i+1
            arr[i][y] = i+1
    
    for row in arr:
        for num in row:
            answer.append(num)
            
    return answer[left:right+1]

# 다른 사람 풀이
def solution2(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer

print(solution(3, 2, 5))
print(solution2(4, 7, 14))