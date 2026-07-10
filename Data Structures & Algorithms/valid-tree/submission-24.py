class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = {}
        if not edges:
            return True

        for edge in edges:
            if edge[0] in edgeMap:
                edgeMap[edge[0]].append(edge[1])
            else:
                edgeMap[edge[0]] = [edge[1]]
            
            if edge[1] in edgeMap:
                edgeMap[edge[1]].append(edge[0])
            else:
                edgeMap[edge[1]] = [edge[0]]

        visited = set()
        def doesCycleExist(node, previous):
            if node in visited:
                return True
            
            neighbours = edgeMap[node]
            visited.add(node)

            for neighbour in neighbours:
                if neighbour == previous:
                    continue
                
                if doesCycleExist(neighbour, node):
                    return True
            return False 
            

        
        if doesCycleExist(0, -1) or not len(visited) == n:
            return False
        return True
            


        