# 내 풀이
def solution(survey, choices):
    answer = ''
    dict = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0, }

    for i in range(len(survey)):
        if choices[i] < 4:
            dict[survey[i][0]] += 4-choices[i]
        elif choices[i] > 4:
            dict[survey[i][1]] += choices[i]-4

    if dict['R'] >= dict['T']:
        answer += "R"
    elif dict['R'] < dict['T']:
        answer += "T"

    if dict['C'] >= dict['F']:
        answer += "C"
    elif dict['C'] < dict['F']:
        answer += "F"

    if dict['J'] >= dict['M']:
        answer += "J"
    elif dict['J'] < dict['M']:
        answer += "M"

    if dict['A'] >= dict['N']:
        answer += "A"
    elif dict['A'] < dict['N']:
        answer += "N"    


    return answer

# 다른 사람 풀이
def solution2(survey, choices):
    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    result = ""
    
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4
            
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution2(["TR", "RT", "TR"], [7, 1, 3]))