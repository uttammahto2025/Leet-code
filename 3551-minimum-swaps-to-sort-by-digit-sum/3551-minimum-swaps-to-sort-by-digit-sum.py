class Solution(object):
    def minSwaps(self, nums):
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        n = len(nums)
        order = sorted(range(n), key=lambda i: (digit_sum(nums[i]), nums[i]))
        target = [0] * n
        for new_pos, i in enumerate(order):
            target[i] = new_pos
        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] or target[i] == i:
                continue
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = target[j]
                cycle_len += 1
            swaps += cycle_len - 1
        return swaps