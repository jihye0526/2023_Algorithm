# 내 풀이
from collections import Counter

def solution(s):
    answer = []
    
    while s:
        if "{" in s: s = s.replace("{", "")
        if "}" in s: s = s.replace("}", "")
        else: break
        
    arr = s.split(",")
    cnt_list = Counter(arr)
    
    while cnt_list:
        answer.append(int(cnt_list.most_common()[0][0]))
        del cnt_list[cnt_list.most_common()[0][0]]
        
    return answer

# 다른 사람 풀이 1
import re

def solution2(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

# 다른 사람 풀이 2 
def solution3(s):
    new_s = [sss.replace('{','').replace('}','') for sss in s.split(',')]
    return [int(c[0]) for c in sorted(Counter(new_s).items(), key = lambda x: x[1],reverse=True )]

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution2("{{20,111},{111}}"))
print(solution2("{{123}}"))
print(solution3("{{4,2,3},{3},{2,3,4,1},{2,3}}"))