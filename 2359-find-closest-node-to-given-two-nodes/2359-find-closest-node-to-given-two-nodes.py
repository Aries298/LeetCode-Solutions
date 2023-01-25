class Solution:
    def dfs(self, node, dist, edges, dis):
        while node != -1 and dis[node] == -1:
            dis[node] = dist
            dist += 1
            node = edges[node]

    def closestMeetingNode(self, edges, node1, node2):
        res, min_dist, n = -1, float('inf'), len(edges)
        dist1, dist2 = [-1]*n, [-1]*n
        self.dfs(node1, 0, edges, dist1)
        self.dfs(node2, 0, edges, dist2)

        for i in range(n):
            if min(dist1[i], dist2[i]) >= 0 and max(dist1[i], dist2[i]) < min_dist:
                min_dist = max(dist1[i], dist2[i])
                res = i
        return res