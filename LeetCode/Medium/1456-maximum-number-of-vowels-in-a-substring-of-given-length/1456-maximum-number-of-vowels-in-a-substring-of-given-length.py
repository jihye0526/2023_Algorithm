import re

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        arr = [1 if i in 'aeiou' else 0 for i in s]
        curr = temp = sum(arr[:k])
        aaa = arr[:k]

        for i in range(k, len(s)):
            temp += arr[i] - arr[i-k]
            curr = max(temp, curr)
            
        return curr