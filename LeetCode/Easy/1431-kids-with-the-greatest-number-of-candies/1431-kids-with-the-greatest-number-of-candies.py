# 내 풀이 1
class Solution1:
    def kidsWithCandies1(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        maxCandy = max(candies)
        
        for i in range(len(candies)):
            temp = candies[i] + extraCandies
            if temp >= maxCandy:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer
    
# 내 풀이 2
class Solution2:
    def kidsWithCandies2(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        maxCandy = max(candies)
        
        for i in range(len(candies)):
            temp = candies[i] + extraCandies
            if temp >= maxCandy:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer
    
# 다른 사람 풀이
class Solution3:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [candy+extraCandies >= maxCandies for candy in candies]