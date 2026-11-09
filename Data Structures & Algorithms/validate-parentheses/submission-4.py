class Solution:
    def isValid(self, s: str) -> bool:
        hm={'}':'{',')':'(',']':'['}
        stack=[]
        for i in s:
            if i in hm:
                if stack and hm[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

        