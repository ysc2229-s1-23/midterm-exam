import heapq

class KthPlusTwoSmallest:
    def __init__(self, nums, k):
        # Initialize the heap with the negative values since heapq is min-heap in Python
        self.heap = [-num for num in nums]
        heapq.heapify(self.heap)
        self.k = k

    def add(self, num):
        if len(self.heap) < self.k + 2:
            return None
        heapq.heappush(self.heap, -num)
        while len(self.heap) > self.k + 2:
            heapq.heappop(self.heap)
        # Return the Kth+2 smallest (which is now negative due to the heap setup)
        return -self.heap[0]
