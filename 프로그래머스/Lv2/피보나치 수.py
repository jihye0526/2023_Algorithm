# 내 풀이
def fibo(arr, i):
    return arr[i-2] + arr[i-1]

def solution(n):
    arr = [0, 1]
    
    for i in range(2, n+1):
        arr.append(fibo(arr, i))
    
    return arr[n]%1234567

# 다른 사람 풀이
def solution2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, (a+b)%1234567
    return a

print(solution(3))
print(solution2(5))