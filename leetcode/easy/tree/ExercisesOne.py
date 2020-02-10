class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, val):
        if self:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self = TreeNode(val)


def print_bfs(node):
    if not node:
        print('None')
        return
    queue = [node]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


def recRangeSumBST(node: TreeNode, L: int, R: int, sum: int) -> int:
    if node:
        if L <= node.val <= R:
            sum += node.val
        if node.left:
            sum += recRangeSumBST(node.left, L, R, 0)
        if node.right:
            sum += recRangeSumBST(node.right, L, R, 0)
    return sum


def rangeSumBST(root: TreeNode, L: int, R: int) -> int:
    return recRangeSumBST(root, L, R, 0)


root = TreeNode(10)
root.insert(7)
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(18)
print(rangeSumBST(root, 7, 15))


def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1 and not t2:
        return None
    result = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
    result.left = mergeTrees(t1 and t1.left, t2 and t2.left)
    result.right = mergeTrees(t1 and t1.right, t2 and t2.right)

    return result


root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)
print('tree 1: ')
print_bfs(root1)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)
print('tree 2: ')
print_bfs(root2)

print('tree merged: ')
print_bfs(mergeTrees(root1, root2))


def searchBST(root: TreeNode, val: int) -> TreeNode:
    if root and root.val == val:
        return root
    if not root:
        return None
    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root = searchBST(root, 2)
print('searched tree: ')
print_bfs(root)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root = searchBST(root, 5)
print('searched tree: ')
print_bfs(root)


def leaves(root: TreeNode):
    res = []
    if not root:
        return res

    queue = [root]
    while len(queue) > 0:
        current = queue.pop()

        if not current.left and not current.right:
            res.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return res

def leafSimilar(root1: TreeNode, root2: TreeNode) -> bool:
    return leaves(root1) == leaves(root2)


root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root2 = TreeNode(2)
root2.left = TreeNode(3)
root2.right = TreeNode(2)
print(leafSimilar(root1, root2))

