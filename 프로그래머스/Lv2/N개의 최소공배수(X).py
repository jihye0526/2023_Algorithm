# 다른 사람 풀이
from math import gcd

def solution(arr):
    answer = arr[0]
    
    for i in arr:
        #1. (arr[0],arr[1])의 최소공배수를 구한 후 answer에 저장
        #2. (#1에서 구한 최소공배수, arr[2])의 최소공배수를 구한 후 answer에 저장
        #3. 모든 배열을 돌면서 최소공배수를 구하고, 저장하고 하는 방식을 진행
        answer = answer*i // gcd(answer, i)     
        
    return answer