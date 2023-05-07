# 내 풀이
def solution1(s):
    answer = ""
    word = ""
    num_arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    dict = {
         "zero":0
        ,"one":1
        ,"two":2
        ,"three":3
        ,"four":4
        ,"five":5
        ,"six":6
        ,"seven":7
        ,"eight":8
        ,"nine":9
    }
    
    for i in s:
        if i in num_arr:
            answer += i
        else:
            word += i
            if word in dict:
                answer += str(dict[word])
                word = ""
            
    return int(answer)

# 다른 사람 풀이
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution2(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

print(solution1("one4seveneight"))
print(solution1("23four5six7"))
print(solution2("2three45sixseven"))
print(solution2("123"))