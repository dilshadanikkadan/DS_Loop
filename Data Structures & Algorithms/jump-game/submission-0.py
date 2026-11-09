class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for index in range(len(nums)):
            if index > farthest:
                return False
            
            curr = index + nums[index]
            farthest = max(curr,farthest)


            if farthest >= len(nums) -1:
                return True    
            
        
        return True