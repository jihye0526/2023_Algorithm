# 내 풀이 1
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums) - nums[0]
        
        if left == right: return 0
        
        for i in range(1, len(nums)):
            left += nums[i-1]
            right -= nums[i]
            if left == right: return i
            
        return -1
    
# 내 풀이 2 - Runtime : 122 ms, Memory : 17.9 MB
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums) - nums[0]
        
        if left == right: return 0
        
        for i in range(1, len(nums)):
            left += nums[i-1]
            right -= nums[i]
            if left == right: return i
            
        return -1