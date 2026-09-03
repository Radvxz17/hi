class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # neet two pointers l , r : buy , sell
        # max profit = sell - buy
        # only update l pointer if found lower price to buy

        l,r = 0 ,1  

        maxP = 0

        #iterate while right pointer has not passed the end of prices

        while r < len(prices):
            if prices[l] < prices[r]: #buy is < sell
                profit = prices[r] - prices[l] #profit is buy - sell
                maxP = max(maxP, profit) #maxP is the max between curr and profi
            else:
                l = r #make l at min
            r += 1
        return maxP

       