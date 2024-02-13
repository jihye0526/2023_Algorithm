class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False

        dict = {}

        a = Counter(word1)
        keys1 = sorted(list(a.keys()))
        values1 = sorted(list(a.values()))
        
        b = Counter(word2)
        keys2 = sorted(list(b.keys()))
        values2 = sorted(list(b.values()))

        return keys1 == keys2 and values1 == values2
        