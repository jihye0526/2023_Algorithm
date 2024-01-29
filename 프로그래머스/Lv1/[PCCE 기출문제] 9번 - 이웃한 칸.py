# 내 풀이
def solution(board, h, w):
    answer = 0
    n = len(board)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = dx[i] + h
        ny = dy[i] + w
        
        if nx >= 0 and nx < n and ny >= 0 and ny < n and board[h][w] == board[nx][ny]:
            answer += 1
             
    return answer

# 다른 사람 풀이
def solution2(board, h, w):
    count = 0
    n = len(board)
    dh, dw = [0,1,-1,0],[1,0,0,-1]
    for i in range(4):
        h_check, w_check = h+dh[i], w+dw[i]
        if 0<=h_check<n and 0<=w_check<n:
            if board[h][w] == board[h_check][w_check]:
                count += 1
    return count

print(solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1))
print(solution([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]], 0, 1))