
public class MostWater {
    public int maxArea(int[] height) {
        
        int n = height.length;
        if(n<=1){return 0;}
        int max =0;
        int l=0 , r=n-1;
        while(l<r)
        {
            int product;
            int dist = r-l;
            product = dist * Math.min(height[l],height[r]);
            if(product>max){max=product;}
            
            if(height[l]>=height[r]){r--;}
            else
            30{l++;}
            if(l==r){break;}
        }
        
        return max;
    }

    public static void main(String[] args) {
        MostWater was = new MostWater();
        int[] h = {4,4,2,11,0,11,5,11,13,8};
        System.out.println(was.maxArea(h));
    }
}   
