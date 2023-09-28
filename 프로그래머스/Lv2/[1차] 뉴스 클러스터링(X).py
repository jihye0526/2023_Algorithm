# 내 풀이(7, 9, 10, 11 틀림)
def solution(str1, str2):
    s = 'abcdefghijklmnopqrstuvwxyz'
    list1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].lower()[0] in s and str1[i:i+2].lower()[1] in s]
    list2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].lower()[0] in s and str2[i:i+2].lower()[1] in s]

    intersection = list(set(list1) & set(list2))
    union = list(set(list1) | set(list2))
    
    for i in intersection:
        min_cnt = min(list1.count(i), list2.count(i))
        max_cnt = max(list1.count(i), list2.count(i))
        intersection = intersection + ([i] * (min_cnt -1))
        union = union + ([i] * (max_cnt -1))
    
    if len(union) != 0:
        return int((len(intersection) / len(union)) * 65536)
    else:
        return 65536
    
# 다른 사람 풀이 1
import re
import math

def solution2(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)

# 다른 사람 풀이 2
from collections import Counter

def solution3(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])
            
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
    
print(solution("FRANCE", "french"))
print(solution2("handshake", "shake hands"))
print(solution3("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))