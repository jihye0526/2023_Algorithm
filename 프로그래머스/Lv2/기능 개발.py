# 내 풀이
from collections import deque

def solution1(progresses, speeds):
    answer = []
    q = deque(progresses) 
    time_q = deque(speeds)
    loc = 0
    
    while q:
        if q[0] >= 100:
            while q:
                if q[0] >= 100:
                    if len(answer) == loc:
                        answer.append(1)
                    else:
                        answer[loc] += 1
                    q.popleft()
                    time_q.popleft()
                else:
                    loc += 1
                    break
        
        for i in range(len(q)):
            if q[i] < 100: q[i] += time_q[i]
    
    return answer

# 다른 사람 풀이 1
def solution2(progresses, speeds):

    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

# 다른 사람 풀이 2
def solution3(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

print(solution1([93, 30, 55], [1, 30, 5]))
print(solution2([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution2([99, 99, 99, 99, 99], [99, 99, 99, 99, 99]))
print(solution3([20, 99, 93, 30, 55, 10], [5, 10, 1, 1, 30, 5]))
print(solution3([1, 99], [99, 1]))