from typing import List


def maxIncreaseKeepingSkyline(grid: List[List[int]]) -> int:
    """
    calculate vertical and horizontal max on the grid
    increase = min(vertical, horizontal) - height
    :param grid:
    :return: increase in height of buildings on the grid, so that the skyline is untouched
    """

    # sorting is (not so much) faster than using max (because of the iterator), and shorter
    #
    # vertical = []
    # horizontal = []
    #
    # for i in range(0, len(grid)):
    #     horizontal.append(max(grid[i]))
    # for i in range(0, len(grid)):
    #     vmax = -1
    #     for j in range(0, len(grid)):
    #         if vmax < grid[j][i]:
    #             vmax = grid[j][i]
    #     vertical.append(vmax)

    n = len(grid)

    vertical = [sorted([row[i] for row in grid])[-1] for i in range(n)]
    horizontal = [sorted(row)[-1] for row in grid]

    res = 0
    for i in range(0, n):
        for j in range(0, n):
            if grid[i][j] < min(horizontal[i], vertical[j]):
                res += min(horizontal[i], vertical[j]) - grid[i][j]
    return res


print(maxIncreaseKeepingSkyline(
    [[3, 0, 8, 4],
     [2, 4, 5, 7],
     [9, 2, 6, 3],
     [0, 3, 1, 0]]))
