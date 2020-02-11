from collections import defaultdict
from typing import List
import heapq
from collections import Counter


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


def search(nums: List[int], target: int) -> int:
    mid = len(nums) // 2
    l = 0
    r = len(nums)
    while l <= r and r >= 0 and l < len(nums):
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))
print(search([-1, 0, 3, 5, 9, 12], 13))


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    res = []
    a = Counter(nums1)
    b = Counter(nums2)
    for k, v in a.items():
        if k in b:
            for i in range(0, min(v, b[k])):
                res.append(k)
    return res


print(intersect([1, 2, 2, 1], [2, 2]))
print(intersect([1, 2, 2, 1], [2]))
print(intersect(
    [43, 85, 49, 2, 83, 2, 39, 99, 15, 70, 39, 27, 71, 3, 88, 5, 19, 5, 68, 34, 7, 41, 84, 2, 13, 85, 12, 54, 7, 9, 13,
     19, 92],
    [10, 8, 53, 63, 58, 83, 26, 10, 58, 3, 61, 56, 55, 38, 81, 29, 69, 55, 86, 23, 91, 44, 9, 98, 41, 48, 41, 16, 42,
     72, 6, 4, 2, 81, 42, 84, 4, 13]))
