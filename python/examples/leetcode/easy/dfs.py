class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def has_path(root, sum):
    if root is None:
        return False

    if root.val == sum and root.left is None and root.right is None:
        return True

    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)

root.left.left = TreeNode(9)

root.right.right = TreeNode(5)
root.right.left = TreeNode(10)

assert has_path(root, 23)
assert has_path(root, 16) == False