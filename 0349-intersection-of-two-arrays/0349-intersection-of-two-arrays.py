class Solution(object):
    def intersection(self, num1, num2):
       new=[]
       for i in range (0,len(num1)):
        for j in range(0,len(num2)):
            if num1[i]==num2[j]:
                new.append(num1[i])
       return list(set(new))
        