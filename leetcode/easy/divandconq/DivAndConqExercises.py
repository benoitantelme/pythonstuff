from collections import defaultdict
from typing import List
import sys


def majorityElement(nums: List[int]) -> int:
    mid = len(nums) // 2
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
        if count[num] > mid:
            return num


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))


def maxSubArray(nums: List[int]) -> int:
    global_max = nums[0]
    local_max = nums[0]
    for i in range(1, len(nums)):
        local_max = max(local_max + nums[i], nums[i])
        global_max = max(local_max, global_max)

    return global_max


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
