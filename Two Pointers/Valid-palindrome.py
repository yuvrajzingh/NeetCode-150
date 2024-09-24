class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1

        while i<j:
            if(s[i].lower() != s[j].lower()):
                if (not s[i].isalnum()):
                    i+=1
                    continue
                elif (not s[j].isalnum()):
                    j-=1
                    continue
                return False
            i+=1
            j-=1
        
        return True