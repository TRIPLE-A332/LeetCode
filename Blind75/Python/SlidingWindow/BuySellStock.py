from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s= 0,1
        highP = 0
        if len(prices) <=1:
            return 0
        
        while s<len(prices):
            profit = prices[s]-prices[b]
            highP = max(highP,profit)

            if profit <= 0:
                b=s
                s+=1
            if profit > 0:
                if s == len(prices)-1:
                    b+=1
                    s=b+1
                else:
                    s+=1
        return highP
