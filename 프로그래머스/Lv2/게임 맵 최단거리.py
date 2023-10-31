# 내 풀이
from collections import deque

def solution(maps):
    answer = 101**2
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque([[0,0,1]])
    
    while q:
        x, y, v = q.popleft()
        
        if x == n-1 and y == m-1:
            answer = min(v, answer)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < n and ny < m and maps[nx][ny] == 1 and visited[nx][ny] == False:
                q.append([nx, ny, v+1])
                visited[nx][ny] = True
    
    return -1 if answer == 101**2 else answer

# 내 풀이(수정)
def solution_update(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque([[0,0,1]])
    
    while q:
        x, y, v = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < n and ny < m and maps[nx][ny] == 1 and visited[nx][ny] == False:
                if nx == n-1 and ny == m-1:
                    return v + 1
                
                q.append([nx, ny, v+1])
                visited[nx][ny] = True
    
    return -1

# 다른 사람 풀이
def solution2(maps):
    x_move = [1, 0, -1, 0]
    y_move = [0, 1, 0, -1]

    x_h, y_h = (len(maps[0]), len(maps))
    queue = deque([(0, 0, 1)])

    while queue:
        x, y, d = queue.popleft()

        for i in range(4):
            nx = x + x_move[i]
            ny = y + y_move[i]

            if nx > -1 and ny > -1 and nx < x_h and ny < y_h:
                if maps[ny][nx] == 1 or maps[ny][nx] > d + 1:
                    maps[ny][nx] = d + 1
                    if nx == x_h - 1 and ny == y_h - 1:
                        return d + 1

                    queue.append((nx, ny, d + 1))

    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution2([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))