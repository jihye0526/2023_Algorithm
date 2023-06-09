# 내 코드
def solution(numbers, hand):
    answer = ''
    left = "*"
    right = "#"
    left_cost = 1000
    right_cost = 1000
    loc = {"1":[0,0], "2":[0,1], "3":[0,2],
           "4":[1,0], "5":[1,1], "6":[1,2],
           "7":[2,0], "8":[2,1], "9":[2,2],
           "*":[3,0], "0":[3,1], "#":[3,2]}
    
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left = i
        elif i in [3, 6, 9]:
            answer += 'R'
            right = i
        else:
            left_cost = abs(loc[str(i)][0] - loc[str(left)][0]) + abs(loc[str(i)][1] - loc[str(left)][1])
            right_cost = abs(loc[str(i)][0] - loc[str(right)][0]) + abs(loc[str(i)][1] - loc[str(right)][1])
            
            if left_cost > right_cost:
                answer += 'R'
                right = i
            elif left_cost < right_cost:
                answer += 'L'
                left = i
            elif left_cost == right_cost:
                answer += hand[0].upper()
                if hand[0] == "r":
                    right = i
                elif hand[0] == "l":
                    left = i
            
    return answer