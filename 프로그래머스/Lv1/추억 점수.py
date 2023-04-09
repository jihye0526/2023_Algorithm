def solution(name, yearning, photo):
    answer = []
    arr = {}
    
    for i in range(len(name)):
        arr[name[i]] = yearning[i]
        
    for i in photo:
        total = 0
        for j in i:
            if j in arr:
                total += arr[j]
        
        answer.append(total)
    
    return answer

def solution2(name, yearning, photos):
    return [sum(yearning[name.index(i)] for i in photo if i in name) for photo in photos]

print(solution2(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]]))