class Solution(object):
    def findTheDifference(self, s, t):       
        for i in t:
            if i not in s :
                return i
            s=s.replace(i,'',1)
        