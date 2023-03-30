def solution(keymap, targets):
    answer = []
    
    for target in targets:
        press = 0

        for char in target:
            flag = False
            cnt = 1000
            
            for key in keymap:
                if char in key:
                    flag = True
                    cnt = min(key.index(char)+1, cnt)

            if not flag:
                press = -1
                break
        
            press += cnt

        answer.append(press)        

    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
print(solution(["AA"], ["B"]))
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))