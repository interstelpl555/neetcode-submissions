class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hp=[]
        for i in nums:
            if i in hp:
                return True
            hp.append(i)
        return False