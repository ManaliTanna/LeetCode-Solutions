def checkIsomorphic(str1, str2):
    i = 0
    my_dict = {}
    while(i < len(str1)):
        if(str1[i] not in my_dict):
            my_dict[str1[i]] = str2[i] #create mapping
        else:
            if( my_dict[str1[i]] != str2[i] ): #check if new character follows the mapping
                return False
        i = i + 1
    return True

class Solution(object):

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False
        else:
            if(checkIsomorphic(s,t) == True and checkIsomorphic(t,s) == True ):
                return True
            else:
                return False







        