"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        def dfs(root, level):
            if root == None:
                return root
            if level == len(ans):
                ans.append([])
            ans[level].append(root.val)
            for child in root.children:
                dfs(child, level + 1)
        ans = []
        dfs(root, 0)
        return ans
            