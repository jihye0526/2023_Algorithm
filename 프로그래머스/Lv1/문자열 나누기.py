# 내 풀이
def solution(s):
    answer = 0
    dict = {"X": 0}

    temp = ""
    for i in range(len(s)):
        if len(dict) == 1:
            dict[s[i]] = 1
            temp = s[i]
        else:
            if s[i] in dict:
                dict[s[i]] += 1
            else:
                dict["X"] += 1
        
        if dict[temp] == dict["X"] or i == len(s)-1:
            answer += 1
            del dict[temp]
            dict["X"] = 0
    
    return answer

# 다른사람 풀이
def solution2(s):
    answer = 0
    sav1=0
    sav2=0
    for i in s:
        if sav1==sav2:
            answer+=1
            a=i
        if i==a:
            sav1+=1
        else:
            sav2+=1
            
    return answer

print(solution("banana"))
print(solution2("abracadabra"))
print(solution("aaabbaccccabba"))