class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        m = len(board)
        n = len(board[0])

        def dfs(i,j,index):
        
            if index == len(word) -1:
                return True

            visited.add((i,j))  
            for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                ni = i + di
                nj = j + dj

                if ni < 0 or ni >= m or nj <0 or nj >= n:
                    continue
                if (ni,nj) in visited:
                    continue

                if board[ni][nj] == word[index + 1]:
                    if dfs(ni,nj,index+1):
                        return True


            visited.remove((i, j))
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]: 
                    res =  dfs(i,j,0) 
                    if res is True:
                        return True
                    
        return False

