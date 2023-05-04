# 다른 사람 풀이1
def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col

# 다른 사람 풀이2
def solution2(sizes):
    print(max(max(x) for x in sizes))
    #return max(max(x) for x in sizes) * max(min(x) for x in sizes)

#print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution2([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution2([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))