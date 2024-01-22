from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        arr = deque(list(s))
        
        for i in t:
            if len(arr) != 0 and i == arr[0]:
                arr.popleft()
        
        return True if len(arr) == 0 else False