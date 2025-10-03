#https://leetcode.com/problems/valid-anagram/description/

from collections import Counter

class SolutionValidAnagram:
    
    def is_anagram(self, input1 : str, input2 : str) -> bool:
        if len(input1) != len(input2):
            return False
        
        return Counter(input1) == Counter(input2)
     
    @staticmethod
    def test_is_anagram(input1: int, input2: int):
        solution = SolutionValidAnagram()
        if solution.is_anagram(input1, input2):
            print("return True is a anagram!")
        else:
            print("return False is not a anagram!")
        