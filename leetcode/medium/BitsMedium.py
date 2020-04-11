from typing import List
from functools import reduce


class Solution:

    def countBits2(self, num: int) -> List[int]:
        result = []
        for i in range(0, num + 1):
            result.append(bin(i).count('1'))
        len([x for x in bin(num) if x == '1'])
        return result

    def countBits(self, num: int) -> List[int]:
        # endup being slower ....
        result = []
        for i in range(0, num + 1):
            y = 0
            while i:
                y += i & 1
                i = i >> 1
            result.append(y)
        return result

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []

        sums = [arr[0]]
        for i in range(1, len(arr)):
            sums.append(sums[i-1] ^ arr[i])

        for lst in queries:
            if lst[0] == lst[1]:
                result.append(arr[lst[0]])
            elif lst[0] > 0:
                result.append(sums[lst[0]-1] ^ sums[lst[1]])
            else:
                result.append(sums[lst[1]])

        return result


sol = Solution()

print(sol.countBits(2))
print(sol.countBits(5))

print(sol.xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]))
