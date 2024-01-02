class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""

        list_word1 = list(map(str, word1))
        list_word2 = list(map(str, word2))

        while list_word1 or list_word2:
            if list_word1:
                answer += list_word1.pop(0)
            if list_word2:
                answer += list_word2.pop(0)

        return answer
    
# 다른 사람 풀이 1
from itertools import zip_longest
# itertools.zip_longest(*iterables, fillvalue=None) 함수는 같은 개수의 자료형을 묶는 파이썬 내장 함수인 zip()과 똑같이 동작
# itertools.zip_longest() 함수는 전달한 반복 가능 객체(*iterables)의 길이가 다르다면 긴 것을 기준으로 빠진 값은 fillvalue에 설정한 값으로 채움
class Solution2:
    def mergeAlternately1(self, word1: str, word2: str) -> str:
        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))
    
# 다른 사람 풀이 2
class Solution2:
    def mergeAlternately2(self, word1: str, word2: str) -> str:
        return "".join(a + b for a, b in zip(word1, word2)) + word1[len(word2):] + word2[len(word1):]