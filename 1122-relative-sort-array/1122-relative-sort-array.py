class Solution(object):
    def relativeSortArray(self, A, B):
        result=[]
        for x in B:
            while x in A:
                result.append(x)
                A.remove(x)
        A.sort()
        Z=result+A
        return Z