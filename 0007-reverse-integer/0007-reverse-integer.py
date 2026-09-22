class Solution(object):
    def reverse(self, x):
            
        A=-1 if x<0 else 1
        x=abs (x)
        R=0
        while x>0:
            num=x%10 
            R=R*10+num 
            x//=10
        R=R*A
        if R<-2**31 or R>2**31-1:
            return 0
        return R 
