# 내 풀이
def solution(n, m):
    answer = [0, 0]
    
    if n > m: n, m = m, n
    
    for i in range(1, n+1):
        if n % i == 0 and m % i == 0: answer[0] = i
        
    answer[1] = n * m / answer[0]
        
    return answer

def gcdlcm(a, b):
    c,d = max(a, b), min(a, b)
    t = 1
    while t>0:
        t = c%d
        c, d = d, t
    answer = [ c, int (a*b/c)]
    return answer

print(solution(3, 4))
print(gcdlcm(3, 12))