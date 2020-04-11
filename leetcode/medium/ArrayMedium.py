import collections
from collections import defaultdict
from typing import List


def diagonalSort(mat: List[List[int]]) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])
    tmp = defaultdict(list)

    # get diagonals on y
    for y in range(m - 1, -1, -1):
        x = 0
        start = (x, y)
        while m > y >= 0 and n > x >= 0:
            tmp[start].append(mat[y][x])
            x += 1
            y += 1

    # get diagonals on x
    for x in range(1, n):
        y = 0
        start = (x, y)
        while m > y >= 0 and n > x >= 0:
            tmp[start].append(mat[y][x])
            x += 1
            y += 1

    # sort diagonals
    for k, v in tmp.items():
        tmp[k] = sorted(v)

    # update matrix
    for k, v in tmp.items():
        x, y = k[0], k[1]
        i = 0
        while m > y >= 0 and n > x >= 0:
            mat[y][x] = v[i]
            x += 1
            y += 1
            i += 1

    return mat


print(diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))


def deckRevealedIncreasing(deck: List[int]) -> List[int]:
    res = collections.deque()
    for card in sorted(deck, reverse=True):
        res.rotate()
        res.appendleft(card)
    return list(res)


print(deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
print(deckRevealedIncreasing([1]))
print(deckRevealedIncreasing([1, 3]))
print(deckRevealedIncreasing([1, 3, 2, 4]))
print(deckRevealedIncreasing([1, 2, 3, 4, 5]))


def matrixScore(A: List[List[int]]) -> int:
    leny = len(A)
    lenx = len(A[0])

    # flip the row if highest value is 0
    for y in range(leny):
        if A[y][0] == 0:
            for x in range(lenx):
                A[y][x] ^= 1

    # flip the column if more 0's than 1's, starting by the second one
    for x in range(1, lenx):
        if sum(row[x] for row in A) < leny / 2:
            for row in A:
                row[x] ^= 1

    res = 0

    # arithmetic shift conversion
    for value in A:
        tmp = 0
        for bit in value:
            tmp = (tmp << 1) | bit
        res += tmp

    return res


print(matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))


def convertToList(L: List[List[int]]) -> List[bool]:
    result = []
    if not L:
        return result

    start = 0
    end = L[len(L) - 1][1]

    while start <= end and L:
        l = L.pop(0)
        if l[0] != start:
            result.extend([False for i in range(l[0] - start)])
            start = l[0]
        result.extend([True for i in range(l[1] - l[0])])
        start = l[1]

    return result


def intersection(a: List[int], b: List[int], n: int):
    return n > 0 and ((a[n] and b[n - 1]) or (a[n - 1] and b[n]))


def intervalIntersection(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    a = convertToList(A)
    b = convertToList(B)

    result = []
    if len(a) == 0 or len(b) == 0:
        return result

    n = 0
    s = 0
    end = min(len(a), len(b))
    while n < end:
        if a[n] and b[n]:
            s = n
            n += 1
            while n < end:
                if a[n] and b[n]:
                    n += 1
                else:
                    result.append([s, n])
                    n += 1
                    s = 0
                    break
        elif intersection(a, b, n):
            result.append([n, n])
            n += 1
        else:
            n += 1

    # close opened interval
    if s != 0:
        result.append([s, n])
    else:
        # check last intersection
        if len(a) > len(b):
            if a[n] and b[n - 1]:
                result.append([n, n])
        else:
            if a[n - 1] and b[n]:
                result.append([n, n])

    return result


print(intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
print(intervalIntersection([], []))
print(intervalIntersection([[1, 7]], [[3, 10]]))
print(intervalIntersection([[5, 8], [15, 18]], [[0, 3], [7, 8], [9, 12]]))
