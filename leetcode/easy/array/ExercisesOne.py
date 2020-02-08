from functools import reduce
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    sub_to_index = {target-v: i for i, v in enumerate(nums)}
    for num in nums:
        if num in sub_to_index and sub_to_index[num] != nums.index(num):
            return [nums.index(num), sub_to_index[num]]


print(twoSum([3, 2, 4], 6))


def decompressRLElist(nums: List[int]) -> List[int]:
    return reduce(lambda a, b: a+b, [[tpl[1]]*tpl[0] for tpl in [nums[i:i + 2] for i in range(0, len(nums), 2)]])


print(decompressRLElist([1, 2, 3, 4]))


def findNumbers2(nums: List[int]) -> int:
    result = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            result += 1

    return result


def findNumbers(nums: List[int]) -> int:
    result = 0
    for num in (num for num in nums if len(str(num))%2 == 0):
        result += 1

    return result


print(findNumbers([12,345,2,6,7896]))


def sumZero(n: int) -> List[int]:
    res = []
    if n % 2 != 0:
        res.append(0)
    for i in range(1, n//2+1):
        res.append(i)
        res.append(-i)

    return res


print(sumZero(5))

