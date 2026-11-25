class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
            out = []
            total = 0
            for x in nums:
                total+=x
                out.append(total)
            return out  
            raise NotImplementedError