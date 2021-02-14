"""
Given a binary tree and a number ‘S’,
find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    dfs(root, [], allPaths, sum)
    return allPaths


def dfs(curr_node, tmp_list, allPaths, sum):
    if not curr_node:
        return

    tmp_list.append(curr_node.val)

    if curr_node.val == sum and curr_node.left is None and curr_node.right is None:
        allPaths.append(list(tmp_list))
    else:
        dfs(curr_node.left, tmp_list, allPaths, sum - curr_node.val)
        dfs(curr_node.right, tmp_list, allPaths, sum - curr_node.val)
    del tmp_list[-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    required_sum = 23
    print("Tree paths with required_sum " + str(required_sum) +
          ": " + str(find_paths(root, required_sum)))


main()
