import copy

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        
        for i in range(len(candies)):
            temp = copy.deepcopy(candies)
            temp[i] += extraCandies
            if temp[i] == max(temp):
                answer.append(True)
            else:
                answer.append(False)
        
        return answer