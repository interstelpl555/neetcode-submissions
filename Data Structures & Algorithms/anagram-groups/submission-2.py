class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for i in strs:
            arr=[0]*26
            for j in i:
                arr[ord(j)-ord('a')]+=1
            arr1=tuple(arr)
            if arr1 not in h:
                h[arr1]=[]
            h[arr1].append(i)
        return [i for a,i in h.items()]