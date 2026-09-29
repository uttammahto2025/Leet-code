class Solution:
    def averageOfSubtree(self, root):
        def dfs(node):
            if not node:
                return 0, 0, 0
            s1, c1, a1 = dfs(node.left)
            s2, c2, a2 = dfs(node.right)
            s = s1 + s2 + node.val
            c = c1 + c2 + 1
            a = a1 + a2
            if s // c == node.val:
                a += 1
            return s, c, a
        return dfs(root)[2]