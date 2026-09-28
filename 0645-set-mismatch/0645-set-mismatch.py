class Solution:
    def findErrorNums(self, nums):
        n =len(nums)
        s =set(nums)
        for i in range(1, n + 1):
            if i not in s:
                KING=i
                break
        temp= sum(nums)-sum(s)
        return [temp, KING]