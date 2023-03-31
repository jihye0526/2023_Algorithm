from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    for word in goal:
        if len(cards1) > 0 and cards1[0] == word:
            cards1.popleft()
            answer = 'Yes'
        elif len(cards2) > 0 and cards2[0] == word:
            cards2.popleft()
            answer = 'Yes'
        else:
            answer = 'No'
            break
            
    return answer

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))