class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for i in strs:
            a="".join(sorted(i))
            if a not in h:
                h[a]=[]
            h[a].append(i)
        b=[i for a,i in h.items()]
        return b
            