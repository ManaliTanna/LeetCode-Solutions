class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # define set of chars in each row
        row0 = set("qwertyuiop")
        row1 = set("asdfghjkl")
        row2 = set("zxcvbnm")

        # helper function to find if chars of the word are a subset of either row
        def made_from_one_row(word):
                chars = set(word.lower())
                return chars <= row0 or chars <= row1 or chars <= row2

        # return only those words which can be made from one row
        return [word for word in words if made_from_one_row(word)]
        
