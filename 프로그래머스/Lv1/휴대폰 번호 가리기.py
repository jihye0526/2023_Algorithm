# 내 풀이
def solution(phone_number):
    return "*" * (len(phone_number)-4) + phone_number[-4::]

solution("01033334444")
solution("027778888")