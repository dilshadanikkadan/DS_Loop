class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        visited = set()

        def dfs(i,j,val):

            if (i,j) not in visited:
                visited.add((i,j))
                dfs(j,n-i-1,matrix[i][j])

            matrix[i][j] = val
                

        for i in range(n):
            for j in range(n):
                if (i,j) not in visited:
                    dfs(j,n-i-1,matrix[i][j])
                
    
