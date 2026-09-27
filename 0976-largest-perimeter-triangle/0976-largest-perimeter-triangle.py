class Solution:
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        for A in range(len(nums)-2):
            if nums[A] <nums[A+ 1] +nums[A + 2]:
                return nums[A] +nums[A+1] +nums[A + 2]
        return 0