# 내 풀이
def solution(a, b):
    answer = ''
    num = 0
    arr = {3:'SUN',4:'MON',5:'TUE',6:'WED',0:'THU',1:'FRI',2:'SAT'}
    
    for i in range(1, a):
        if i in [1,3,5,7,8,10,12]:
            num += 31    
        elif i == 2:
            num += 29
        else:
            num += 30

    num += b

    return arr[num%7]

# 다른 사람 풀이 1
def solution1(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]


# 다른 사람 풀이 2
import datetime

def solution2(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]
    
print(solution(5, 24))
print(solution1(5, 24))
print(solution2(5, 24))