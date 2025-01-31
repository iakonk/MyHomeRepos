
https://leetcode.com/problems/serialize-and-deserialize-bst
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # [1, 2, '', '',3, 4,'','', 5, '', '']
        acc = []

        def dfs(node):
            if node:
                acc.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                acc.append('')
                return

        dfs(root)

        return ','.join(acc)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # [1, 2, '', '', 3, 4, '', '', 5, '', '']
        acc = data.split(',')

        def dfs():
            curr_val = acc.popleft()
            if not curr_val:
                return ''
            node = TreeNode(curr_val)
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

    # Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))