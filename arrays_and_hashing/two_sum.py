#https://leetcode.com/problems/two-sum/
from typing import List

class SolutionTwoSum:
    
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        result= []
        for i, num in enumerate(nums):            
            size = len(nums)
            print(f"índice: {i}, valor: {num}, size: {size}")
            if (size - 1) > i:
                print(nums[i])
                if (nums[i] + nums[i + 1]) == target:
                    result.append(i)
                    result.append(i+1)
        return result