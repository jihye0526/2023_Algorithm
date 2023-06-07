# 내 풀이
def solution(N, stages):
    answer = []
    
    for i in range(1, N+1):
        cnt = stages.count(i)
        ratio = len([x for x in stages if x >= i])
        
        if cnt == 0:
            answer.append([i, 0])
        else:
            answer.append([i, cnt/ratio])
        
    return [i[0] for i in sorted(answer, key=lambda x:x[1], reverse=True)]

# 다른 사람 풀이
def solution2(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    print(info)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):]) # 레벨에 도달했고 다 푼 사람
        yet = info[i + 1] # 레벨에 도달했지만 못 푼 사람
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution2(4, [4,4,4,4,4]))