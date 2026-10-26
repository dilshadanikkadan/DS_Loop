class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        vertices = {}
        has_cycle = False
        visted = set()
        stack = set()

        for v in prerequisites:
            if v[1] not in vertices:
                vertices[v[1]] = {v[0]} 
                if v[0] not in vertices:
                    vertices[v[0]]  = set()
            else:
                vertices[v[1]].add(v[0])
                if v[0] not in vertices:
                    vertices[v[0]]  = set()

        def dfs(vertex):
            nonlocal has_cycle
            if has_cycle is True:
                return
        
            visted.add(vertex)
            stack.add(vertex)
            for v in vertices[vertex]:
                if v not in visted:
                    dfs(v)
                elif v in stack:
                    has_cycle = True    
            stack.remove(vertex)        

        for v in vertices:
            if has_cycle is True:
                break
            if v not in visted:
                dfs(v)
                
        
        print(vertices)
        return True if has_cycle is False else False