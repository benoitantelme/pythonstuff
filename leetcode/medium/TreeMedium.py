# Definition for a binary tree node.
from typing import List


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
            sum[depth - 1] += current.val
        if current.left:
            stack.append((current.left, depth + 1))
        if current.right:
            stack.append((current.right, depth + 1))

    return sum[len(sum) - 1]


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
print('Sum grand parents: ')
print(sumEvenGrandparent(root))


def in_order_dfs_rewrite(current: TreeNode, total: int) -> int:
    if current.left:
        total = in_order_dfs_rewrite(current.left, total)
    tmp = current.val
    current.val = total
    total = total - tmp
    if current.right:
        total = in_order_dfs_rewrite(current.right, total)
    return total


def bstToGst(root: TreeNode) -> TreeNode:
    # get total with bfs
    total = 0
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        total += current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    in_order_dfs_rewrite(root, total)
    return root


root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.left.right.right = TreeNode(3)
root.right.right.right = TreeNode(8)
print('Values modified:')
bfs_print(bstToGst(root))


def recInsertIntoBST(current: TreeNode, val: int):
    if current.val > val:
        if not current.left:
            current.left = TreeNode(val)
        else:
            recInsertIntoBST(current.left, val)
    else:
        if not current.right:
            current.right = TreeNode(val)
        else:
            recInsertIntoBST(current.right, val)


def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    if not root:
        root = TreeNode(val)
    else:
        recInsertIntoBST(root, val)
    return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print('Tree is:')
bfs_print(root)
print('after inserting:')
bfs_print(insertIntoBST(root, 5))


def recConstructMaximumBinaryTree(nums: List[int]) -> TreeNode:
    if len(nums) == 0:
        return None

    maximum = max(nums)
    top_node = TreeNode(maximum)
    middle = nums.index(maximum)
    top_node.left = recConstructMaximumBinaryTree(nums[:middle])
    top_node.right = recConstructMaximumBinaryTree(nums[middle + 1:])
    return top_node


def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
    return recConstructMaximumBinaryTree(nums)


print('constructed tree:')
print(bfs_print(constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])))
