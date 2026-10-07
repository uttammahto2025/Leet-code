class Solution(object):
    def xorOperation(self, n, start):
        temp=0
        for i in range(n) :
            temp^=(start+2*i)
        return temp


        