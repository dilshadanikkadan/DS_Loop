class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visted = set()
        m = len(matrix)
        n = len(matrix[0])
        total_el = m* n
    

        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        res = []


        i = 0
        j = 0
        curr_index_dir= 0
        prev_i= 0
        prev_j = 0

        while True:
            if len(res) == total_el:
                break

            if i < 0 or i >= m or j <0 or j>=n:
                i = prev_i
                j = prev_j
                curr_index_dir = (curr_index_dir + 1 ) % len(dir)   
                i,j = i+dir[curr_index_dir][0],j+dir[curr_index_dir][1]
                
            if (i,j) in visted:
                print(f"i and j in vitest{(i,j)}")
                curr_index_dir = (curr_index_dir + 1 ) % len(dir)
                i = prev_i
                j = prev_j
                i,j = i+dir[curr_index_dir][0],j+dir[curr_index_dir][1]

            res.append(matrix[i][j])
            visted.add((i,j))
            prev_i = i
            prev_j = j
            i,j = i+dir[curr_index_dir][0],j+dir[curr_index_dir][1]
    
        return res

 


