# 다른 사람 풀이
def solution(dirs):
    arr = set()
    loc = (0, 0)
    dict = {"U":(0, 1), "D":(0, -1), "L": (-1, 0), "R": (1, 0)}
    
    for dir in dirs:
        temp = dict[dir]
        nx = loc[0] + temp[0]
        ny = loc[1] + temp[1]
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            arr.add(((loc[0], loc[1]), (nx, ny)))
            arr.add(((nx, ny), (loc[0], loc[1])))
            loc = (nx, ny)

    return len(arr)//2

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("UDLRDURL"))