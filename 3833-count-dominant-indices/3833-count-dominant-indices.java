class Solution {
    public int dominantIndices(int[] nums) {
        int n = nums.length;
        int Count = 0;
        long rightSum = 0;
        for (int i = n - 1; i >= 0; i--) {
            int rightCount = n - 1 - i;
            if (rightCount > 0 && (long) nums[i] * rightCount > rightSum) {
                Count++;
            }
            rightSum += nums[i];
        }
        return Count;
    }
}