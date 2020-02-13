from collections import defaultdict
from typing import List


def groupThePeople(groupSizes: List[int]) -> List[List[int]]:
    res = []
    size_to_list = defaultdict(list)
    for i in range(0, len(groupSizes)):
        length = groupSizes[i]
        size_to_list[length].append(i)
        if len(size_to_list[length]) == length:
            res.append(size_to_list[length])
            size_to_list[length] = []

    return res


print(groupThePeople([3, 3, 3, 3, 3, 1, 3]))
print(groupThePeople([2, 1, 3, 3, 3, 2]))
