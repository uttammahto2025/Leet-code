class Solution:
    def countStudents(self, students, sandwiches):
        K= [0, 0]
        for x in students:
            K[x] +=1
        for x in sandwiches:
            if K[x]== 0:
                break
            K[x] -=1
        return K[0]+K[1]