# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.my_set = set()
        self.dfs(root, 0)


    def dfs(self, n, val):
        if n is None:
            return
        else:
            n.val = val
            self.my_set.add(val)
            self.dfs(n.left, 2*val + 1)
            self.dfs(n.right, 2*val + 2)

    def find(self, target: int) -> bool:
        if target in self.my_set:
            return True
        else:
            return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)