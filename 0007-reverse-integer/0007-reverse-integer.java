class Solution {
    public int reverse(int x) {
        int R = 0;
        while (x!= 0) {
            int digit=x%10;
            x /= 10;
            if (R >Integer.MAX_VALUE / 10 || (R == Integer.MAX_VALUE / 10 && digit > 7))
            {
                return 0;
            }
            if ( R < Integer.MIN_VALUE / 10 || (R == Integer.MIN_VALUE / 10 && digit < -8)) 
            {
                return 0;
            }
            R = R*10+digit;
        }
        return R;
    }
}