class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        status=[0]*(n)
        res=[]
        
        def dfs(i):# this function will check is there any loop, cycle and i is a part of that loop,cycle 
            if status[i]=="visited": #if this node is already visited, loop detected return true
                return True
            if status[i]=="safe": #if this node is previously visited and marked safe no need to repeat it ,return False no loop possible from it
                return False
            status[i]="visited" # so we have visited this node
            for j in graph[i]:
                if  dfs(j):# if loop detected return True
                    return True
            status[i]="safe" # if we reached till here means no loop detected from node i so this node is safe
            return False # no loop possible return false
       
    
        for i in range(n):
            if not dfs(i): #if no loop detected this node is safe 
                res.append(i)
        return res