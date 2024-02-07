class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr).values()
        
        if len(set(cnt)) == len(cnt):
            return True

        return False