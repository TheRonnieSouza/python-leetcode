from arrays_and_hashing.contains_duplicate import Solution
from arrays_and_hashing.valid_anagram import SolutionValidAnagram
from arrays_and_hashing.group_anagrams import SolutionGroupAnagrams
from two_pointers.valid_palindrome import SolutionValidPalindrome

## -------------------

palindrome = SolutionValidPalindrome()

#string = "A man, a plan, a canal: Panama"
#string = "race a car"
string = "    "

if palindrome.isPalindrome(s= string):
    print(f"o texto -> {string} <-- is a palindrome")
else:
    print(f"o texto -> {string} <-- is not a palindrome")

## ------------------   groupAnagrams  ---------------


#group_anagrams = SolutionGroupAnagrams()

#strs = ["eat","tea","tan","ate","nat","bat"]
#result = group_anagrams.groupAnagrams(strs)
#print(f" the result is : {result}")


## ------------------   test_is_anagram  ---------------

#Solution.TestContainsDuplicate(1,2,3,1)

#SolutionValidAnagram.test_is_anagram("teste", "ttees")


