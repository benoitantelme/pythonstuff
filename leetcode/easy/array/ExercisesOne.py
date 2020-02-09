from functools import reduce
from typing import List
from collections import Counter
import sys


def twoSum(nums: List[int], target: int) -> List[int]:
    sub_to_index = {target - v: i for i, v in enumerate(nums)}
    for num in nums:
        if num in sub_to_index and sub_to_index[num] != nums.index(num):
            return [nums.index(num), sub_to_index[num]]


print(twoSum([3, 2, 4], 6))


def decompressRLElist(nums: List[int]) -> List[int]:
    return reduce(lambda a, b: a + b, [[tpl[1]] * tpl[0] for tpl in [nums[i:i + 2] for i in range(0, len(nums), 2)]])


print(decompressRLElist([1, 2, 3, 4]))


def findNumbers2(nums: List[int]) -> int:
    result = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            result += 1

    return result


def findNumbers(nums: List[int]) -> int:
    result = 0
    for num in (num for num in nums if len(str(num)) % 2 == 0):
        result += 1

    return result


print(findNumbers([12, 345, 2, 6, 7896]))


def sumZero(n: int) -> List[int]:
    res = []
    if n % 2 != 0:
        res.append(0)
    for i in range(1, n // 2 + 1):
        res.append(i)
        res.append(-i)

    return res


print(sumZero(5))


def sortedSquares(A: List[int]) -> List[int]:
    return [x ** 2 for x in sorted(A, key=lambda x: abs(x))]


print(sortedSquares([-4, -1, 0, 3, 10]))


def countCharacters(words: List[str], chars: str) -> int:
    res = 0
    ref = Counter(chars)
    for word in words:
        if not Counter(word) - ref:
            res += len(word)

    return res


print(countCharacters(["ccat", "bt", "hat", "tree"], "atach"))


def fib(N: int) -> int:
    a = 0
    if N == 0:
        return a
    b = 1
    if N == 1:
        return b

    res = 1
    for i in range(2, N+1):
        tmp = a
        a = b
        b += tmp
        res += tmp

    return res


print(fib(4))


def minCostToMoveChips(chips: List[int]) -> int:
    odd = 0
    even = 0

    for chip in chips:
        if chip % 2 == 0:
            even += 1
        else:
            odd += 1

    if even > odd:
        parity = True
    else:
        parity = False

    res = 0
    for chip in chips:
        if chip % 2 == 0 ^ parity:
            res += 1

    return res


print(minCostToMoveChips([2, 2, 2, 3, 3]))


def maxProfitSingle(prices: List[int]) -> int:
    if not prices:
        return 0

    min = sys.maxsize
    result = -sys.maxsize - 1
    for price in prices:
        if price < min:
            min = price
        if result < price - min:
            result = price - min

    return result


print(maxProfitSingle([7, 1, 5, 3, 6, 4]))
print(maxProfitSingle([7, 6, 4, 3, 1]))


def maxProfit(prices: List[int]) -> int:
    res = 0
    for tpl in [prices[i:i+2] for i in range(0, len(prices)-1)]:
        if tpl[0] < tpl[1]:
            res += tpl[1]-tpl[0]

    return res


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([1, 2, 3, 4, 5]))
