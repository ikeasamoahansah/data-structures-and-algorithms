
class TreeNode:
    def __init__(self, val):
        self.parent = TreeNode 
        self.left = TreeNode | None
        self.right = TreeNode | None
        self.val = val
    
    def BSTPreorder(self):
        def walk(TreeNode: curr, path):
            if curr is None:
                return path
            path.append(curr.val)
            walk(curr.left, path)
            walk(curr.right, path)

            return path

        def pre_order_search(TreeNode: head):
            return walk(head, list: path)

    def BSTInorder(self):
        def walk(TreeNode: curr, path):
            if curr is None:
                return path
            walk(curr.left, path)
            path.append(curr.val)
            walk(curr.right, path)

            return path

        def in_order_search(TreeNode: head):
            return walk(head, list: path)

    def BSTPostorder(self):
        def walk(TreeNode: curr, path):
            if curr is None:
                return path
            walk(curr.left, path)
            walk(curr.right, path)
            path.append(curr.val)

            return path

        def post_order_search(TreeNode: head):
            return walk(head, List: path)

