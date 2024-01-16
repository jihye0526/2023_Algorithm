class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
        