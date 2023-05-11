# 내 풀이
def solution(answers):
    answer = []
    counts = [0,0,0]
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == first[i%len(first)]: counts[0] += 1
        if answers[i] == second[i%len(second)]: counts[1] += 1
        if answers[i] == third[i%len(third)]: counts[2] += 1
    
    for i in range(len(counts)):
        if counts[i] == max(counts):
            answer.append(i+1)
        
    return answer

# 다른 사람 풀이
def solution2(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers): # 다른점 : enumerate 사용
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score): # 다른점 : enumerate 사용
        if s == max(score):
            result.append(idx+1)

    return result

print(solution([1,2,3,4,5]));
print(solution([1,3,2,4,2]));