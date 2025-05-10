import heapq


class Median:
    def __init__(self):
        self.small, self.large = [], []

    def insert(self, num):
        heapq.heappush(self.small, -1 * num)
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def get_median(self):
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2


media = Median()
media.insert(5)
media.insert(4)
media.insert(3)
media.insert(7)
print(media.get_median())  # 4.5
