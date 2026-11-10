class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        post=1
        pre=1
        fin=[1]*n
        for i in range(n):
            fin[i]*=pre
            fin[n-i-1]*=post
            pre*=nums[i]
            post*=nums[n-i-1]
        return fin
