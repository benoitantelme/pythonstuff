from collections import defaultdict
from typing import List
import heapq


def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True

    i = 0
    j = 0
    while i < len(t):
        if t[i] == s[j]:
            j += 1
            if j == len(s):
                return True
        i += 1

    return False


print(isSubsequence("abc", "ahbgdc"))


def peakIndexInMountainArray(A: List[int]) -> int:
    i = 1
    while i < len(A):
        if A[i] < A[i - 1]:
            return i - 1
        i += 1


print(peakIndexInMountainArray([0, 2, 1, 0]))


def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    count_to_index = defaultdict(list)
    heap = []
    i = 0
    while i < len(mat):
        row = mat[i]
        count = 0
        while count < len(row) and row[count] == 1:
            count += 1
        heapq.heappush(heap, count)
        count_to_index[count].append(i)
        i += 1

    res = []
    while len(res) < k:
        lst = count_to_index[heapq.heappop(heap)]
        while len(lst) > 0 and len(res) < k:
            res.append(lst.pop(0))
    return res


print(kWeakestRows(
    [[1, 1, 0, 0, 0],
     [1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [1, 1, 1, 1, 1]], 3))

print(kWeakestRows(
    [[1, 0, 0, 0],
     [1, 1, 1, 1],
     [1, 0, 0, 0],
     [1, 0, 0, 0]], 2))

