class Solution:
    def reverseVowels(self, s):
        v = "aeiouAEIOU"
        a = [x for x in s if x in v]
        a.reverse()
        j = 0
        ans = ""
        for x in s:
            if x in v:
                ans += a[j]
                j += 1
            else:
                ans += x
        return ans