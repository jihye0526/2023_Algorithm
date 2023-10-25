# 다른 사람 풀이
from collections import deque

def solution(n, wires):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        visited = [0] * (n+1)
        q = deque([start])
        visited[start] = 1
        cnt = 1
        
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
        return cnt
            
    answer = n
    
    for a,b in wires:
        #graph에서 remove
        graph[a].remove(b)
        graph[b].remove(a)
        
        answer = min(abs(bfs(a) - bfs(b)), answer)
        
        #다시 append
        graph[a].append(b)
        graph[b].append(a)
    
    return answer

# 다른 사람 풀이 2
def solution2(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        [s.update(v) for _ in sub for v in sub if set(v) & s] # 집합연산자 & : 교집합 연산,   집합연산자 update : 여러데이터를 한번에 추가
        ans = min(ans, abs(2 * len(s) - n))
    return ans

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution2(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))