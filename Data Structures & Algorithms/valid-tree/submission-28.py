class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True 

        adjMap = {}
        for edge in edges:
            if edge[0] in adjMap:
                adjMap[edge[0]].append(edge[1])
            else:
                adjMap[edge[0]] = [edge[1]]
            

            if edge[1] in adjMap:
                adjMap[edge[1]].append(edge[0])
            else:
                adjMap[edge[1]] = [edge[0]]
            

        visited = set()
        def doesCycleExist(current, previous):
            if current in visited:
                return True
            
            if current not in adjMap:
                return False
            
            visited.add(current)
            neighbours = adjMap[current]

            for neighbour in neighbours:
                if neighbour == previous:
                    continue
                
                if doesCycleExist(neighbour, current):
                    return True
            return False
        
        if doesCycleExist(0, -1) or len(visited) != n:
            return False
        return True

            
        



        

        