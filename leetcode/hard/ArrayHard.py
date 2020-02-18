from typing import List


def trap(height: List[int]) -> int:
    maxl = 0
    water = []
    result = 0

    # left to right
    for i in height:
        if i >= maxl:
            tmp_min = min(maxl, i)
            result += sum([tmp_min - x if tmp_min - x > 0 else 0 for x in water])
            water.clear()
            maxl = i
        else:
            water.append(i)

    # right to left with the rest to find water trapped by a maximum on the left
    if len(water) > 0:
        height = height[len(height) - len(water) - 1:]
        maxr = 0
        water = []
        for i in reversed(height):
            if i >= maxr:
                tmp_min = min(i, maxr)
                result += sum([tmp_min - x if tmp_min - x > 0 else 0 for x in water])
                water.clear()
                maxr = i
            else:
                water.append(i)

    return result


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap([4, 2, 3]))
