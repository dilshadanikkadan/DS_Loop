class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_bits(num):
            count = 0
            while num:
                count += (num &1)
                num >>= 1
            return count

        res = []
        for i in range(n+1):
            res.append(count_bits(i)) 
        return res              