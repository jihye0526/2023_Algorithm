# 내 풀이
class Solution1:
    def findDifference1(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []

        nums1_set = set(nums1)
        nums2_set = set(nums2)

        intersection = nums1_set & nums2_set

        answer.append(list(nums1_set -intersection))
        answer.append(list(nums2_set -intersection))

        return answer
    
# 다른 사람 풀이
class Solution2:
    def findDifference2(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        a = list(set1 - set2)
        b = list(set2 - set1)
        
        return [a, b]