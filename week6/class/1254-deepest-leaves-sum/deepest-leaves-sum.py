# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        deepest_sum = depth = 0
        stack = [(root, 0)]
        while stack :
            node, curr_depth = stack.pop()
            if node.left is None and node.right is None:
                if depth < curr_depth:
                    deepest_sum = node.val #reset sum for the new deepest depth
                    depth = curr_depth
                elif depth == curr_depth:
                    deepest_sum += node.val
            else:
                if node.right:
                    stack.append((node.right, curr_depth + 1))
                if node.left:
                    stack.append((node.left, curr_depth + 1))
        return deepest_sum

        