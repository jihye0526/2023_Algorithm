# 내 풀이
import numpy as np

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        answer = 0 
        temp = np.transpose(grid)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row] == list(map(int, temp[col])):
                    answer += 1
        
        return answer
    
# 다른 사람 풀이
class Solution2:
    def equalPairs2(self, grid: List[List[int]]) -> int:
        m = defaultdict(int)
        cnt = 0

        for row in grid:
            m[str(row)] += 1

        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cnt += m[str(col)]
        return cnt    