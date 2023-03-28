def solution(wallpaper):
    answer = []
    x = []
    y = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if "#" in wallpaper[i][j]:
                x.append(i)
                y.append(j)

    answer = [min(x), min(y), max(x)+1, max(y)+1]
    return answer

print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))