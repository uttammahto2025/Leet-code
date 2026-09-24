class Solution(object):
    def isHappy(self, n):
        while n!=1 and n!=4:
            a=0
            while n>0:
                x=n%10
                a+=x*x
                n=n//10
            n=a
        if n==1:
                return True 
        else :
                 return False 