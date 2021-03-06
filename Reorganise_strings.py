class Solution:
    def reorganizeString(self, S: str) -> str:
        heap = [(-S.count(x),(x)) for x in set(S)]
        heapq.heapify(heap)
        # print(heapq.heappop(heap))
        # print(heapq.heappop(heap))
        if any(-nc > (len(S)+1)/2 for nc,x in heap):
            return ""
        ans = []
        while len(heap) >= 2:
            nct1, ch1 = heapq.heappop(heap)
            nct2, ch2 = heapq.heappop(heap)
            
            ans.extend([ch1, ch2])
            if nct1 + 1 != 0:
                heapq.heappush(heap, (nct1 + 1, ch1))
            if nct2 + 1 != 0:
                heapq.heappush(heap, (nct2 + 1, ch2))

        return "".join(ans) + (heap[0][1] if heap else "")
            
        