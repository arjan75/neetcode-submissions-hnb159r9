class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True 
            
        neighbours = {}
        for edge in edges:
            if edge[0] in neighbours:
                neighbours[edge[0]].append(edge[1])
            else:
                neighbours[edge[0]] = [edge[1]]
            
            if edge[1] in neighbours:
                neighbours[edge[1]].append(edge[0])
            else:
                neighbours[edge[1]] = [edge[0]]
        
        visited = set()
        def traverse(node, previous):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbour in neighbours[node]:
                if neighbour == previous:
                    continue
                
                if neighbour in visited:
                    return False
                
                if not traverse(neighbour, node):
                    return False
            return True        

        if traverse(0, -1) and len(visited) == n:
            return True
        return False
        