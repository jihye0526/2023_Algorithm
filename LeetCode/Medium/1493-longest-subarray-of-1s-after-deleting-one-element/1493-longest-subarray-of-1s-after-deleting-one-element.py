# 내 풀이
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = 0
        k = 1

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            if k < 0:
                if nums[left] == 0:
                    k += 1

                left += 1

        return right - left

# 다른 사람 풀이
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        answer = 0
        left = zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                
                left += 1

            answer = max(answer, right - left + 1 - zeros)

        return answer -1 if answer == len(nums) else answer