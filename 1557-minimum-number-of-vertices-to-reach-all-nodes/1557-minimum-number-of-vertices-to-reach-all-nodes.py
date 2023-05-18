class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create an indegree list of size n and initialize all elements to 0.
        indegree = [0] * n
        # Iterate through all the edges and update the indegree of each node.
        for edge in edges:
            indegree[edge[1]] += 1
        # Create an answer list.
        ans = []
        # Iterate through all the vertices and add the ones with an indegree of 0 to the answer list.
        for i in range(n):
            if indegree[i] == 0:
                ans.append(i)
        # Return the answer list.
        return ans