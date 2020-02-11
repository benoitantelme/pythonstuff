# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def maxDepth(root: 'Node') -> int:
    if not root:
        return 0

    max_depth = 1
    stack = [(root, max_depth)]

    while len(stack) > 0:
        current, depth = stack.pop(0)
        if depth > max_depth:
            max_depth = depth
        if current.children:
            for child in current.children:
                stack.append((child, depth + 1))

    return max_depth


five = Node(5)
six = Node(6)
three = Node(3, [five, six])
two = Node(2)
four = Node(4)
root = Node(1, [two, three, four])
print(maxDepth(root))



# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


def getImportance(employees: List['Employee'], id: int) -> int:
    dict = {}
    for employee in employees:
        dict[employee.id] = employee

    sum = 0
    stack = [dict[id]]
    while len(stack) > 0:
        current = stack.pop(0)
        sum += current.importance
        if current.subordinates:
            for sub_id in current.subordinates:
                stack.append(dict[sub_id])
    return sum


two = Employee(2, 3, None)
three = Employee(3, 3, None)
one = Employee(1, 5, [2, 3])
print(getImportance([one, two, three], 1))

