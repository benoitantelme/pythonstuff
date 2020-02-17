
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
