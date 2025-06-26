# Palindrome check
def isPalindrome(x): #1st
        """
        :type x: int
        :rtype: bool
        """
        return (str(x) == str(x)[::-1])
