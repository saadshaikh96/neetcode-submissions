class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        import heapq
        heap = []
        heapq.heapify(heap)

        for num, frequency in counts.items():
            heapq.heappush(heap, (frequency, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [pair[1] for pair in heap]
        