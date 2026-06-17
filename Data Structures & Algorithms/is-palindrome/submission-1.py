class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s2 = ''.join(ch.upper() for ch in s if ch.isalnum())
        
        l,r = 0, len(s2)-1

        while l<r :
            if s2[l] == s2[r]:
                l += 1
                r -= 1
            else:
                return False

        return True


        