def solution(park, routes):
    answer = []
    start = []
    d = {
        "E" : [0, 1],
        "W" : [0, -1],
        "S" : [1, 0],
        "N" : [-1, 0]
    }
    
    W, H = len(park[0]), len(park)
    
    for i in range(H):
        for j in range(W):
            if "S" in park[i][j]:
                start = [i, j]
                break
    
    for route in routes:
        isBoolean = False
        dir, step = route.split(" ")
        step = int(step)
        
        for i in range(1, step+1):
            dx = start[0] + (d[dir][0] * i)
            dy = start[1] + (d[dir][1] * i)
            
            if dx < 0 or dy < 0 or dx >= H or dy >= W:
                isBoolean = True
                break
            if "X" in park[dx][dy]:
                isBoolean = True
                break
            
        if isBoolean : continue
        start = [dx, dy]
    
    return start

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))