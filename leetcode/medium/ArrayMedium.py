from collections import defaultdict
from typing import List


def diagonalSort(mat: List[List[int]]) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])
    tmp = defaultdict(list)

    # get diagonals on y
    for y in range(m-1, -1, -1):
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
