class Solution:
    def isValid(self, s):
        stack = []
        for x in s:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            else:
                if not stack:
                    return False
                a = stack.pop()
                if x == ')' and a != '(':
                    return False
                if x == '}' and a != '{':
                    return False
                if x == ']' and a != '[':
                    return False           
        return len(stack) == 0