from typing import List


class Solution:

    def countBits2(self, num: int) -> List[int]:
        result = []
        for i in range(0, num+1):
            result.append(bin(i).count('1'))
        len([x for x in bin(num) if x == '1'])
        return result

    def countBits(self, num: int) -> List[int]:
        # endup being slower ....
        result = []
        for i in range(0, num+1):
            y = 0
            while i:
                y += i & 1
                i = i >> 1
            result.append(y)
        return result


sol = Solution()

print(sol.countBits(2))
print(sol.countBits(5))


