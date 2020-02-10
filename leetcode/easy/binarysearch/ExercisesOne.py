from typing import List


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
        if A[i] < A[i-1]:
            return i-1
        i += 1


print(peakIndexInMountainArray([0, 2, 1, 0]))

