# 내 풀이
from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        arr = deque(list(s))
        
        for i in t:
            if len(arr) != 0 and i == arr[0]:
                arr.popleft()
        
        return True if len(arr) == 0 else False

# 다른 사람 풀이
class Solution2:
    def isSubsequence2(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)