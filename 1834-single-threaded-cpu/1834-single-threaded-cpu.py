class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        i, heap, time = 0, [], tasks[0][0]
        while len(ans) < len(tasks):
            while (i < len(tasks)) and (tasks[i][0] <= time):
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if heap:
                time_diff, origin_idx = heapq.heappop(heap)
                time += time_diff
                ans.append(origin_idx)
            elif i < len(tasks): time = tasks[i][0]
        return ans