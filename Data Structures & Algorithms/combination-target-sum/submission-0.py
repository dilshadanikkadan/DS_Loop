class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        current = []
        res = []

        def backtrack(start,sum):
            if sum == target:
                res.append(current.copy())
                return
            if sum > target:
                return

            for i in range(start,len(nums)):
                current.append(nums[i])

                backtrack(i,sum + nums[i])
                
                current.pop()
        
        backtrack(0,0)    
        return res


