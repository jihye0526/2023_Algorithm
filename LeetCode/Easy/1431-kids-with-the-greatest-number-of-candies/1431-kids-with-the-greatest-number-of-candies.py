class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        maxCandy = max(candies)
        
        for i in range(len(candies)):
            temp = candies[i] + extraCandies
            if temp >= maxCandy:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer