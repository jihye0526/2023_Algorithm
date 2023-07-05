# 다른 사람 풀이 1
from collections import deque

def solution(board):
    N = len(board)
    M = len(board[0])
    q = deque()
    dist = [[101 for _ in range(M)] for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(len(board)):
        j = board[i].find('R')
        if j != -1:
            q.append((i, j, 0))
            dist[i][j] = 0
            break
        
    while q:
        x, y, c = q.popleft()
        
        if board[x][y] == 'G':
            return c
        
        for i in range(4):
            nx = x
            ny = y
            
            while 0<=nx+dx[i]<N and 0<=ny+dy[i]<M and board[nx+dx[i]][ny+dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
                
            if dist[nx][ny] > c+1:
                dist[nx][ny] = c+1
                q.append((nx, ny, c+1))
        
    return -1

# 다른 사람 풀이 2
def solution2(board):
    answer = -1
    
    N, M = len(board), len(board[0])

    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for x in range(N):
        for y in range(M):
            if board[x][y] == "R":
                sx, sy = x, y
    
    visited = [[False]*M for _ in range(N)]

    q = deque()

    q.append((sx, sy, 0))
    
    while q:
        x, y, level = q.popleft()
        
        if board[x][y] == "G":
            answer = level
            break
        
        # 한방향으로 미끄러져 이동
        for dx, dy in direction:
            scope = 1
            while 1:
                nx, ny = x+dx*scope, y+dy*scope
                
                if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny] == "D":
                    if visited[nx-dx][ny-dy] == False:
                        visited[nx-dx][ny-dy] = True
                        q.append((nx-dx, ny-dy, level+1))
                    
                    break
                
                scope += 1
    
    
    
    return answer

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution2([".D.R", "....", ".G..", "...D"]))