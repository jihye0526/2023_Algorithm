# 내 풀이
def solution(elements):
    answer = set()
    double = elements * 2
    
    for i in range(1, len(elements)+1):
        for j in range(len(double)):
            answer.add(sum(double[j:j+i]))
            
    return len(answer)

# 다른 사람 풀이
def solution2(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)

print(solution([7,9,1,1,4]))
print(solution2([7,9,1,1,4]))