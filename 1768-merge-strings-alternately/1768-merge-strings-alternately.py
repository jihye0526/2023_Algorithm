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