#https://leetcode.com/problems/valid-palindrome/description/

class SolutionValidPalindrome:
    
     def isPalindrome(self, s: str) -> bool:
        s_filtered = ''.join(ch.lower() for ch in s if ch.isalnum())     
        return s_filtered == s_filtered[::-1]
    
