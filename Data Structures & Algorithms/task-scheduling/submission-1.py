class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        frequency = {}
        for task in tasks:
            if task in frequency:
                frequency[task] = frequency[task] + 1
            else:
                frequency[task] = 1
        
        maxHeap = []
        for key, value in frequency.items():
            heapq.heappush_max(maxHeap, value)

        time = 0
        queue = deque()
        while maxHeap or queue:
            time += 1
            if maxHeap:
                taskFreq = heapq.heappop_max(maxHeap) - 1
                taskCooldown = time + n
                if taskFreq > 0:
                    queue.append((taskFreq, taskCooldown))
            
            if queue and time == queue[0][1]:
                heapq.heappush_max(maxHeap, queue.popleft()[0])
        
        return time
            



        