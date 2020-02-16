from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return 'Node: ' + self.val


def getOrderedList(current: TreeNode, ordered : List[int]):
    """
    DFS in order to get the ordered list
    """
    if current:
        getOrderedList(current.left, ordered)
        ordered.append(current.val)
        getOrderedList(current.right, ordered)


def mergeLists(list1: List[int], list2: List[int]) -> List[int]:
    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list1[i])
            i += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result


def getAllElements(root1: TreeNode, root2: TreeNode) -> List[int]:
    list1 = []
    getOrderedList(root1, list1)
    list2 = []
    getOrderedList(root2, list2)

    return mergeLists(list1, list2)


root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)
print(getAllElements(root1, root2))
