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
                