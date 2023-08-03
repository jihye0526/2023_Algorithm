# 다른 사람 풀이
def solution(n):
    if n<3:
        return n
    
    d = [0]*(n+1)
    d[1] = 1
    d[2] = 2
    
    # n-2 칸을 뛴 후에 + 2칸을 더 뛴다
    # n-1 칸을 뛴 후에 + 1칸을 더 뛴다
    for i in range(3,n+1):
        d[i] = d[i-1] + d[i-2]
        
    return d[n]%1234567

print(solution(4))
print(solution(3))