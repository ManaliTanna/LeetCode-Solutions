class Solution:
    def isPalindrome(self, s: str) -> bool:

        # function to determine if a character is non alphanumeric
        def is_non_alphanumeric(c):
            if c in '0123456789':
                return False
            elif c in 'abcdefghijklmnopqrstuvwxyz':
                return False
            else:
                return True

        # pointer to track characters starting from the left
        l_ptr = 0

        # pointer to track characters starting from the right
        r_ptr = len(s)-1

        #convert string to lowercase
        s = s.lower()

        # until pointers dont exceed bound
        while s and r_ptr>0 and l_ptr<len(s) and l_ptr < r_ptr:

            #ignore character if non alphanumeric
            while s and is_non_alphanumeric(s[l_ptr]) and l_ptr < r_ptr:
                l_ptr = l_ptr + 1
            while s and is_non_alphanumeric(s[r_ptr]) and l_ptr < r_ptr:
                r_ptr = r_ptr - 1

            # if characters on both side are not equal return False
            if s[l_ptr] != s[r_ptr]:
                return False
            
            # Move the pointer in correct direction
            l_ptr = l_ptr + 1
            r_ptr = r_ptr - 1
        
        return True

