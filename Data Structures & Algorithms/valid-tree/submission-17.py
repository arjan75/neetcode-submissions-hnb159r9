class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        nodeMap = {}
        if not edges:
            return True
            
        for edge in edges:
            if edge[0] in nodeMap:
                nodeMap[edge[0]].append(edge[1])
            else:
                nodeMap[edge[0]] = [edge[1]]
            
            if edge[1] in nodeMap:
                nodeMap[edge[1]].append(edge[0])
            else:
                nodeMap[edge[1]] = [edge[0]]
        
        def doesCycleExist(current, previous):
            if current not in nodeMap:
                return False
            
            if current in visited:
                return True
            
            neighbours = nodeMap[current]
            visited.add(current)
            for neighbour in neighbours:
                if neighbour == previous:
                    continue
                
                if doesCycleExist(neighbour, current):
                    return True

            return False
        
        if doesCycleExist(0, -1) or len(visited) != n:
            return False
        return True
            





        