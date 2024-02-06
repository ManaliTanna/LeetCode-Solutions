class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
    
        for word in strs:
            # Sort the characters of the word to create a unique key for anagrams
            sorted_word = ''.join(sorted(word))
        
            # Check if the sorted_word is already in the hash table
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    
        # Convert the values of the hash table to a list to get the final result
        result = list(anagrams.values())
    
        return result
        