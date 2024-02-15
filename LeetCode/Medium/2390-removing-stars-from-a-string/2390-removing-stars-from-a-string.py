class Solution:
    def removeStars(self, s: str) -> str:
        arr = []
        
        for i in s:
            if i != "*":
                arr.append(i)
            elif i == "*" and len(arr) != 0:
                arr.pop()

        return "".join(arr)