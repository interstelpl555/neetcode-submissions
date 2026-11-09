class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if l<r and not self.an(s[l]):
                l=l+1
                continue
            if l<r and not self.an(s[r]):
                r-=1
                continue
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True

    def an(self,c):
        return (ord('A')<=ord(c)<=ord('Z')) or (ord('0')<=ord(c)<=ord('9'))or (ord('a')<=ord(c)<=ord('z'))

        

        
