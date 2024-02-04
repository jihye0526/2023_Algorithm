class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = [0]

        for i, val in enumerate(gain):
            answer.append(answer[i] + val)

        return max(answer)