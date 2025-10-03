#https://leetcode.com/problems/contains-duplicate/description/



from typing import List

class Solution:
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
    def containsDuplicateOptmized(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    @staticmethod
    def TestContainsDuplicate(num1: int, num2: int, num3: int, num4: int):
        nums = [num1,num2,num3,num4]
        solution = Solution()
        
        if solution.containsDuplicate(nums):
            print("solution 1 : return True -> Contain repited numbers")
        else:
            print("solution 1 : return False -> not contain repited numbers")
            
        if solution.containsDuplicateOptmized(nums):
            print("solution 2 : return True -> Contain repited numbers")
        else:
            print("solution 2 : return False -> not contain repited numbers")
        