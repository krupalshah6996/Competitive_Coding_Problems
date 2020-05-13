def leastInterval(self, tasks: List[str], n: int) -> int:
        current_time = 0
        heap = [(-tasks.count(x),x) for x in set(tasks)]
        heapq.heapify(heap)
        # print(heap)
        while heap:
            index, temp = 0, []
            while index <= n:
                current_time += 1
                if heap:
                    timing, taskid = heappop(heap)
                    # We're checking to see if it's at the end of the overall count. 
                    # Remember that it was negative at the beginning
                    if timing != -1:
                        temp.append((timing+1, taskid))
                # Checking to see if we're out of tasks. Exit the inner loop if both are true.
                # This will automatically exit out of the overall tasks 
                if not heap and not temp:
                    break
                else:
                    index += 1
            for item in temp:
                heappush(heap, item)
        return current_time
                    
        #Mathematical Solution
        # tasks_count = list(collections.Counter(tasks).values())
        # max_count = max(tasks_count)
        # max_count_tasks = tasks_count.count(max_count)
        # return max(len(tasks), (max_count-1)*(n+1)+max_count_tasks)   