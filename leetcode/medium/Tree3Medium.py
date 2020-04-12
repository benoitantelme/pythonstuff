
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'node:' + str(self.val)


class FindElements:

    def __init__(self, root: TreeNode):
        self.set = set()
        root.val = 0
        stack = [root]
        while len(stack) > 0:
            current = stack.pop()
            self.set.add(current.val)

            if current.left:
                current.left.val = 2 * current.val + 1
                stack.append(current.left)
            if current.right:
                current.right.val = 2 * current.val + 2
                stack.append(current.right)

        self.root = root

    def find(self, target: int) -> bool:
        return target in self.set


root = TreeNode(-1)
root.right = TreeNode(-1)
f = FindElements(root)
print(f.find(1))
print(f.find(2))


class LowestCommonAncestor:
    def height(self, node: TreeNode) -> int:
        if not node:
            return 0

        l = self.height(node.left)
        r = self.height(node.right)
        return max(l, r) + 1

    def recPostOrder(self, node: TreeNode, depth: int, height: int) -> TreeNode:
        if node is None:
            return None

        if node.left is None and node.right is None and depth == height:
            return node

        left = self.recPostOrder(node.left, depth + 1, height)
        right = self.recPostOrder(node.right, depth + 1, height)

        if left is None:
            return right
        if right is None:
            return left
        return node


    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        height = self.height(root)
        return self.recPostOrder(root, 1, height)


lca = LowestCommonAncestor()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
res = lca.lcaDeepestLeaves(root)
print(res)

root.left.left = TreeNode(4)
res = lca.lcaDeepestLeaves(root)
print(res)

root.left.right = TreeNode(5)
res = lca.lcaDeepestLeaves(root)
print(res)
