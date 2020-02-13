
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    queue = [(root, 1)]
    max_depth = 0
    while len(queue) > 0:
        current, depth = queue.pop(len(queue)-1)
        if depth > max_depth:
            max_depth = depth
        if current.left:
            queue.append((current.left, depth + 1))
        if current.right:
            queue.append((current.right, depth + 1))

    return max_depth


eight = TreeNode(8)
seven = TreeNode(7)
nine = TreeNode(9)
three = TreeNode(3)
three.left = eight
three.right = seven
root = TreeNode(1)
root.left = three
root.right = nine
print(maxDepth(root))


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    queue = [(p, q)]
    while len(queue) > 0:
        l, r = queue.pop(len(queue)-1)
        if not l and not r:
            continue
        elif not l or not r:
            return False
        elif l.val != r.val:
            return False
        else:
            queue.append((l.left, r.left))
            queue.append((l.right, r.right))

    return True


two = TreeNode(2)
three = TreeNode(3)
one = TreeNode(1)
one.left = two
one.right = three
print(isSameTree(one, one))

two = TreeNode(2)
three = TreeNode(3)
one = TreeNode(1)
one.left = two
one.right = three
onetwo = TreeNode(1)
onetwo.left = three
onetwo.right = two
print(isSameTree(one, onetwo))

