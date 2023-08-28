# 내 풀이
def solution(cards):
    visited = [False] * len(cards)
    arr = []
    
    while False in visited:
        loc = visited.index(False)
        temp = []
        
        while visited[loc] != True:
            visited[loc] = True
            loc = cards[loc]-1
            temp.append(cards[loc])
        
        arr.append(len(temp))
        
    arr.sort(key=lambda x:-x)
            
    return 0 if len(arr) < 2 else arr[0] * arr[1]

# 다른 사람 풀이
def solution2(cards):
    answer = []
    for i in range(len(cards)):
        tmp = []
        while cards[i] not in tmp:
            tmp.append(cards[i])
            i = cards[i] - 1
        answer.append([] if sorted(tmp) in answer else sorted(tmp))
    answer.sort(key=len)

    return len(answer[-1]) * len(answer[-2])

print(solution([8,6,3,7,2,5,1,4]))
print(solution2([8,6,3,7,2,5,1,4]))