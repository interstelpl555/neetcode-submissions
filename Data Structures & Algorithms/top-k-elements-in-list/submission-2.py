class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp={}
        arr=[[] for i in range(len(nums)+1)]
        for i in nums:
            hp[i]=hp.get(i,0)+1
        for i,j in hp.items():
            arr[j].append(i)
        res=[]
        for i in range(len(arr)-1,0,-1):
            for j in arr[i]:
                res.append(j)
                if len(res)==k:
                    return res

            
