from typing import List


class Solution:

    def countBits(self, num: int) -> List[int]:
        result = []
        for i in range(0, num+1):
            result.append(len([x for x in bin(i) if x == '1']))
        len([x for x in bin(num) if x == '1'])
        return result


sol = Solution()

print(sol.countBits(2))
print(sol.countBits(5))


