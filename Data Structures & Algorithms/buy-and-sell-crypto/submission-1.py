class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        m=0
        while(r<len(prices)):
            if prices[r]>prices[l]:
                d=prices[r]-prices[l]
                m=max(m,d)
            else: l=r
            r+=1
        return m