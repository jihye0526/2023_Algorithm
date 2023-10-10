# 내 풀이
def solution(files):
    answer = []
    
    for file in files:
        text = ''
        num = ''
        for idx, s in enumerate(file):
            if not s.isnumeric():
                text += s.lower()
            elif s.isnumeric():
                num += s
            
            if idx == len(file)-1 or len(num) != 0 and idx != len(file)-1 and not file[idx+1].isnumeric():
                answer.append([text, int(num), file])
                break
        
    answer.sort(key=lambda x:(x[0], x[1]))
    
    return [i[2] for i in answer]

# 다른 사람 풀이
import re

def solution2(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution2(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(["O00321", "O49qcGPHuRLR5FEfoO00321"]))