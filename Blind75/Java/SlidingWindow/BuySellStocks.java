package Blind75.SlidingWindow;

public class BuySellStocks {

    public int maxProfit(int[] prices) {

        int max = 0;        
        int n = prices.length-1;
        if(prices.length<=1){return 0;}
        int l = 0 , r= l+1;
        while(r<=n)
        {
            if(prices[l]>prices[r])
            {
                l=r;
                r++;
                continue;
            }
            if(prices[l]==prices[r]){r++;continue;}
            if(prices[l]<prices[r])
            {
                int diff = prices[r]-prices[l];
                max = Math.max(max , diff);
                r++;
            }
        }
        
        return max;
    }
    public static void main(String[] args) {
        BuySellStocks bs = new BuySellStocks();
        int[] prices = {1,2};
        System.out.println(bs.maxProfit(prices));
    }
}
