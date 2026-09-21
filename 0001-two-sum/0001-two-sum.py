class Solution(object):
    def twoSum(self, nums, target):
        p=len(nums)
        for i in range (0,p):
            for j in range (i+1,p):
                if nums[i]+nums[j]==target:
                    return i,j