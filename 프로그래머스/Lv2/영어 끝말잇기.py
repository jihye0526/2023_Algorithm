# 내 풀이
def solution(n, words):
    answer = [0, 0]
    arr = []
    cnt = 0

    for i, word in enumerate(words):
        if i % n == 0: cnt += 1
        
        if len(arr) == 0: arr.append(word)
        elif arr[-1][-1] == word[0] and word not in arr:
            arr.append(word)
        else:
            answer = [(i % n)+1, cnt]
            break
        
    return answer

# 다른 사람 풀이
def solution2(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution2(2, ["hello", "one", "even", "never", "now", "world", "draw"]))