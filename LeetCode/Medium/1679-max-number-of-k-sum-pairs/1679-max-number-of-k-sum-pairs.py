class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        answer = 0
        left, right = 0, len(nums)-1

        while left < right:
            add = nums[left] + nums[right]
            if add == k:
                left += 1
                right -= 1
                answer += 1
            elif add < k:
                left += 1
            else:
                right -= 1

        return answer
            