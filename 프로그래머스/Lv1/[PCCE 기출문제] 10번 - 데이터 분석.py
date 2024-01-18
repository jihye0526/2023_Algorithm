# 내 풀이
def solution(data, ext, val_ext, sort_by):
    answer = []
    dict = {"code": 0, "date": 1, "maximum":2, "remain":3}
    
    for temp in data:
        if temp[dict[ext]] < val_ext:
            answer.append(temp)
            
        answer.sort(key=lambda x:x[dict[sort_by]])
        
    return answer

# 내 풀이
def solution2(data, ext, val_ext, sort_by):
    answer = []
    arr = ["code", "date", "maximum", "remain"]

    for temp in data:
        if temp[arr.index(ext)] < val_ext:
            answer.append(temp)

        answer.sort(key=lambda x:x[arr.index(sort_by)])
    return answer

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))
print(solution2([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))