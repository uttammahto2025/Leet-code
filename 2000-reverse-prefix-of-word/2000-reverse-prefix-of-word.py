class Solution:
    def reversePrefix(self, word, ch):
        for i in range(len(word)):
            if word[i] == ch:
                Temp=word[:i+ 1]
                S= word[i + 1:]
                return Temp[::-1] + S
        return word