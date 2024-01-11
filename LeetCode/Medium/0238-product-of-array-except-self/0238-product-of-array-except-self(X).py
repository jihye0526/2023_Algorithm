# 다른 사람 풀이
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        pre = 1
        post = 1
        
        for i in range(length):
            answer[i] *= pre
            pre = pre * nums[i]
            answer[length-i-1] *= post
            post = post * nums[length-i-1]

        return answer