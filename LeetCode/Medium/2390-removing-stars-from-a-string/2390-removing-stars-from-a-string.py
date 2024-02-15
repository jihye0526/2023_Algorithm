# 내 풀이
class Solution:
    def removeStars(self, s: str) -> str:
        arr = []
        
        for i in s:
            if i != "*":
                arr.append(i)
            elif i == "*" and len(arr) != 0:
                arr.pop()

        return "".join(arr)
    
# 다른 사람 풀이
class Solution2:
    def removeStars2(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch is '*':
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)