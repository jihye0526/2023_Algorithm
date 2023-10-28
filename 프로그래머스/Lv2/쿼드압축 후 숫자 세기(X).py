# 다른 사람 풀이 
def solution(arr):
    answer = [0, 0]
    length = len(arr)
    
    def compression(a,b,n):
        start = arr[a][b]
        
        for i in range(a, a+n):
            for j in range(b, b+n):
                if arr[i][j] != start:
                    n = n // 2
                    compression(a, b, n)
                    compression(a, b+n, n)
                    compression(a+n, b, n)
                    compression(a+n, b+n, n)
                    return
                    
        answer[start] += 1
    
    compression(0, 0, length)
    
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))