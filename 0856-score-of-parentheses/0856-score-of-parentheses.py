class Solution(object):
    def scoreOfParentheses(self, s):
        TEMP= depth = 0
        for i in range(len(s)):
            if s[i]=='(':
                depth+=1
            else:
                depth-=1
                if s[i-1] == '(':
                    TEMP+= 1<< depth
        return TEMP