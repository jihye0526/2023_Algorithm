# 내 풀이
def solution(data, col, row_begin, row_end):
    answer = 0
    temp = []
    data = sorted(data, key=lambda x:(x[col-1], -x[0]))
    
    for i in range(row_begin-1, row_end):
        temp.append(sum([num % (i+1) for num in data[i]]))
    
    for i in temp:
        answer ^= i
        
    return answer

# 다른 사람 풀이
from functools import reduce

def solution2(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col-1], -x[0]))
    return reduce(lambda x, y: x ^ y,
                  [sum(map(lambda x: x%(i+1), data[i])) for i in range(row_begin-1, row_end)])
    
print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]]))
print(solution2([[2,2,6],[1,5,10],[4,2,9],[3,8,3]]))