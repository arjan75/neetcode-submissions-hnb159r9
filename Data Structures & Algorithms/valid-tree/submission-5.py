class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n or not edges: 
            return True
            
        adjList = {}
        for edge in edges:
            if edge[0] in adjList:
                adjList[edge[0]].append(edge[1])
            else:
                adjList[edge[0]] = [edge[1]]
            
            if edge[1] in adjList:
                adjList[edge[1]].append(edge[0])
            else:
                adjList[edge[1]] = [edge[0]]
        
        visited = set()
        def traverse(node, previous):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbour in adjList[node]:
                if neighbour == previous:
                    continue
                
                if not traverse(neighbour, node):
                    return False
            
            return True
        return traverse(0, -1) and len(visited) == n
            
        