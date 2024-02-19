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