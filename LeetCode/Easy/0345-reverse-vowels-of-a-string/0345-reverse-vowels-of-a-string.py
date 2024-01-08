# 내 풀이 1
class Solution:
    def reverseVowels(self, s: str) -> str:
        answer = ""
        
        s_list= list(map(str, s))
        vowels_list = [i for i in s_list if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]
        vowels_list.reverse()
        
        for i in s_list:
            if i not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                answer += i
            else:
                answer += vowels_list.pop(0)
                
        return answer
                
# 내 풀이 2
class Solution:
    def reverseVowels(self, s: str) -> str:
        answer = ""
        vowels_list = [i for i in s if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]
        
        for i in s:
            if i not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                answer += i
            else:
                answer += vowels_list.pop()
                
        return answer

# 다른 사람 풀이
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s)-1
        vowels = 'aeiouAEIOU'

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
        
        return ''.join(s)