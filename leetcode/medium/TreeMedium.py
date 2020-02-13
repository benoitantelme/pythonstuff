# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bfs_print(root: TreeNode):
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)



def deepestLeavesSum(root: TreeNode) -> int:
    sum = []
    stack = [(root, 1)]
    while len(stack) > 0:
        current, depth = stack.pop()
        if len(sum) < depth:
            sum.append(current.val)
        else:
            sum[depth-1] += current.val
        if current.left:
            stack.append((current.left, depth+1))
        if current.right:
            stack.append((current.right, depth+1))

    return sum[len(sum)-1]




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(7)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(8)
print("Tree in bfs:")
bfs_print(root)
print(deepestLeavesSum(root))


def sumEvenGrandparent(root: TreeNode) -> int:
    sum = 0
    stack = [(root, None, None)]

    while len(stack) > 0:
        current, parent, grandparent = stack.pop()
        if grandparent and grandparent.val % 2 == 0:
            sum += current.val
        if current.left:
            stack.append((current.left, current, parent))
        if current.right:
            stack.append((current.right, current, parent))

    return sum


root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
print(sumEvenGrandparent(root))

