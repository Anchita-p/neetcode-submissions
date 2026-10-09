class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0 #buy
        r=1 #sell
        maxprofit=0

        while r<len(prices):
            #profitable?
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxprofit=max(profit,maxprofit)
            #got more lower price to buy
            else:
                l=r
            #iterating to check every price to get the most profitable price and updating accordingly
            r+=1
        return maxprofit
