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