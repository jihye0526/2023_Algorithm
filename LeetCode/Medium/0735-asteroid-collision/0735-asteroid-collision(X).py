# 다른 사람 풀이1
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        temp = []

        for asteroid in asteroids:
            while temp and temp[-1] > 0 and asteroid < 0:
                if temp[-1] + asteroid < 0: 
                    temp.pop()
                elif temp[-1] + asteroid > 0: 
                    break
                else: 
                    temp.pop()
                    break
            else: temp.append(asteroid)

        return temp
    
# 다른 사람 풀이2
class Solution2:
    def asteroidCollision2(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 > a:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue
                elif stack[-1] == abs(a):
                    stack.pop()
                break # this means asteroid must be destroyed (not add to stack in else statement below)
            else:
                stack.append(a)
        
        return stack