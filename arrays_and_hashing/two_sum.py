#https://leetcode.com/problems/two-sum/
from typing import List

class SolutionTwoSum:
    
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        mapa = {}
        
        for i, num in enumerate(nums):
            complemento = target - num 
            if complemento in mapa:
                return [mapa[complemento], i]
            mapa[num] = i