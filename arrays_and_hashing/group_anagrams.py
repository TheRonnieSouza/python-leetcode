#https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
from typing import List

class SolutionGroupAnagrams:
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        base = ord('a')
        grupos = defaultdict(list)
        
        for s in strs:
            print(f"\n current word: {s}")
            count = [0]*26
            print(f"\n current count: {count}")
            for c in s:
                index = ord(c) - base
                count[index] += 1
                print(f" Letter '{c}' -> index {index} -> count: {count[index]}")
                print(f"\n current count: {count}")
            key = tuple(count)
            print(f"   Final signature for this word: key = {key}")
            grupos[key].append(s)
            print(f"Current state of grupos:")
            for k, v in grupos.items():
                print(f" key and value:     {k}: {v}")
            
        print("\n=== Final grouped result ===")
        print(list(grupos.values()))
        return list(grupos.values())
        

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            hashmap["".join(sorted(s))].append(s)

        return list(hashmap.values())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''       
        
 “Alright, I’m going to solve the Group Anagrams problem, but I’ll walk you through it step by step so you can see exactly how it works.”

from collections import defaultdict


“I start by importing defaultdict from the collections module, because it allows me to create a dictionary that automatically initializes a list for new keys — this way, I don’t need to check if a key exists before adding an item.”

def groupAnagrams(strs):


“Here I define a function called groupAnagrams, which takes a list of strings named strs.”

    base = ord('a')
    groups = defaultdict(list)


“base stores the numeric code of the letter 'a', which I’ll use to convert each letter into an index from 0 to 25.
groups is a defaultdict(list), meaning every key starts automatically with an empty list.”

    for s in strs:
        print(f"\n Current word: {s}")
        count = [0]*26


“Now, for each word in strs, I create a count array with 26 zeros — one for each letter in the English alphabet.
This array represents the signature of the word, that is, how many times each letter appears.”

        for c in s:
            index = ord(c) - base
            count[index] += 1
            print(f"   Letter '{c}' → index {index} → count: {count[index]}")


“Then I loop through each character in the word.
ord(c) converts the character to its numeric code, and subtracting ord('a') gives me the position of that letter in the alphabet — zero for ‘a’, one for ‘b’, nineteen for ‘t’, and so on.
I increment the corresponding position in the count array.
The print statement just helps visualize what’s happening — which letter, which index, and the updated count.”

        key = tuple(count)
        print(f"    Final signature for this word: {key}")


“After counting the letters, I convert the list into a tuple — since lists can’t be used as dictionary keys.
This tuple acts as a unique signature for the group of anagrams: words with the same signature belong to the same group.”

        groups[key].append(s)
        print(f"    Current state of groups:")
        for k, v in groups.items():
            print(f"      {k}: {v}")


“Here I append the current word to the correct group based on its signature.
And I print the current state of the dictionary to see how the groups are being formed step by step.”

    print("\n=== Final grouped result ===")
    print(list(groups.values()))
    return list(groups.values())


“Finally, I return only the values of the dictionary — which are lists of words that are anagrams of each other.”

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])


“And here I test it with a sample input.
The output should look like [["eat","tea","ate"], ["tan","nat"], ["bat"]], showing that the algorithm correctly grouped the anagrams.”

 Extra :

“This solution runs in O(n·k) time, where n is the number of words and k is the average word length.
It’s optimal because instead of sorting each string (O(k log k)), I count the letters in linear time (O(k)), which makes it faster for large datasets.”

'''
