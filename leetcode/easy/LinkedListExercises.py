
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getDecimalValue(head: ListNode) -> int:
    as_str = str()
    current = head
    while current:
        as_str += str(current.val)
        current = current.next

    return int(as_str, 2)


# [1, 0, 1]
root = ListNode(1)
root.next = ListNode(0)
root.next.next = ListNode(1)
print(getDecimalValue(root))


def middleNode(head: ListNode) -> ListNode:
    size = 0
    current = head
    while current:
        size += 1
        current = current.next

    current = head
    for i in range(0, size//2):
        current = current.next

    return current


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
print(middleNode(root))


def reverseList(head: ListNode) -> ListNode:
    if not head:
        return None

    new_node = ListNode(head.val)
    new_node.next = None

    while head.next:
        head = head.next
        tmp = ListNode(head.val)
        tmp.next = new_node
        new_node = tmp

    return new_node


print(reverseList(root))


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    val1 = l1.val
    val2 = l2.val

    if val1 < val2:
        head = ListNode(val1)
        l1 = l1.next
    else:
        head = ListNode(val2)
        l2 = l2.next

    tmp = head
    while l1 and l2:
        if l1.val < l2.val:
            tmp.next = ListNode(l1.val)
            l1 = l1.next
        else:
            tmp.next = ListNode(l2.val)
            l2 = l2.next
        tmp = tmp.next

    while l1:
        tmp.next = ListNode(l1.val)
        l1 = l1.next
        tmp = tmp.next
    while l2:
        tmp.next = ListNode(l2.val)
        l2 = l2.next
        tmp = tmp.next

    return head


root1 = ListNode(1)
root1.next = ListNode(3)
root1.next.next = ListNode(4)
root2 = ListNode(1)
root2.next = ListNode(2)
root2.next.next = ListNode(4)
print(mergeTwoLists(root1, root2))


def hasCycle(head: ListNode) -> bool:
    visited = set()
    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next

    return False


root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(-4)
root.next.next.next.next = root
print(hasCycle(root))

