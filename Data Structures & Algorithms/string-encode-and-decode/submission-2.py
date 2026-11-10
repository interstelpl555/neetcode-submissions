class Solution:

    def encode(self, strs: List[str]) -> str:
        a=3 
        s=""
        for i in strs:
            for j in i:
                n=ord(j)+a
                s+=chr(n)
            s+=" "
        return s

    def decode(self, s: str) -> List[str]:
        a=3
        o=[]
        d=""
        for i in s:
            if i==" ":
                o.append(d)
                d=""
            else:
                d+=chr(ord(i)-a)
        return o