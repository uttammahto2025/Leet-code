class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            if i and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            l, r = i + 1, n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    a, b = nums[l], nums[r]
                    while l < r and nums[l] == a:
                        l += 1
                    while l < r and nums[r] == b:
                        r -= 1

        return res