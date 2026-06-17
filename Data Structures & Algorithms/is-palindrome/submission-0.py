class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #clean_s = "".join(char for char in s if char.isalnum())
        clean_s = re.sub(r'[^a-zA-Z0-9]','',s)


        if clean_s.upper() == clean_s[::-1].upper():
            return True
        else:
            return False