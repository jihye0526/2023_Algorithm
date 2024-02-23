class RecentCounter:

    def __init__(self): 
        self.answer = []

    def ping(self, t: int) -> int:
        self.answer.append(t)
        while self.answer[0] < t-3000:
            self.answer.pop(0)

        return len(self.answer)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)