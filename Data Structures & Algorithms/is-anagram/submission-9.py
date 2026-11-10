class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a=[0]*26
        for i in range(len(s)):
            diff=ord(s[i])-ord('a')
            diff1=ord(t[i])-ord('a')
            a[diff]+=1
            a[diff1]-=1
        for i in a:
            if i!=0:
                return False
        return True