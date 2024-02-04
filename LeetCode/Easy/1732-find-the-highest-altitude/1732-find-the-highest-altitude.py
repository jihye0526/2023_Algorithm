# 내 풀이 1
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = [0]

        for i, val in enumerate(gain):
            answer.append(answer[i] + val)

        return max(answer)
    
# 내 풀이 2
class Solution2:
    def largestAltitude2(self, gain: List[int]) -> int:
        start = 0
        answer = 0

        for val in gain:
            start += val
            answer = max(start, answer)

        return answer