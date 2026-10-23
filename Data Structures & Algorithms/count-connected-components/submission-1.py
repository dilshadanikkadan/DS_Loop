class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vertices = {}
        visited = set()
        for v in edges:
            if v[0] not in vertices:
                vertices[v[0]] = {v[1]}
                if v[1] not in vertices:
                    vertices[v[1]] = {v[0]}
                else:
                    vertices[v[1]].add(v[0])           
            else:
                
                vertices[v[0]].add(v[1])  
                if v[1] not in vertices:
                    vertices[v[1]] = {v[0]}
                else:
                    vertices[v[1]].add(v[0])         

        def dfs(vertex):
            visited.add(vertex)
            for v in vertices[vertex]:
                if v not in visited:
                    dfs(v)

        count = 0
        for v in vertices:
            if v not in visited:
                count +=1
                dfs(v)   
        if len(visited) != n:
            count +=1        

        return count