# 다른 사람 풀이
answer = 0

def solution(k, dungeons):
    global answer    
    v = [False] * len(dungeons)
    dfs(k, 0, dungeons, v)
    return answer

def dfs(k, cnt, dungeons, v):
    global answer
    if cnt > answer:
        answer = cnt
    
    for i, dungeon in enumerate(dungeons):
        a, b = dungeon

        if not v[i] and k >= a:
            v[i] = True
            dfs(k-b, cnt+1, dungeons, v)
            v[i] = False

print(solution(80, [[80,20],[50,40],[30,10]]))