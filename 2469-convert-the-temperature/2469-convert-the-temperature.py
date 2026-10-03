class Solution(object):
    def convertTemperature(self, c):
        K=c+273.15
        ans= c* 1.80 + 32.00
        return [K,ans]
       
        