from typing import List


def get_str(s):
    res = str()
    for l in s:
        if l == '#':
            if len(s) > 0:
                res = res[:-1]
        else:
            res += l

    return res


def backspaceCompare(S: str, T: str) -> bool:
    return get_str(S) == get_str(T)


print(backspaceCompare("ab#c", "ad#c"))
print(backspaceCompare("ab##", "c#d#"))


def twoSum(numbers: List[int], target: int) -> List[int]:
    diff = {}
    for i in range(0, len(numbers)):
        if numbers[i] in diff:
            return diff[numbers[i]] + 1, i + 1
        else:
            diff[target - numbers[i]] = i
        i += 1


print(twoSum([2, 7, 11, 15], 9))


def moveZeroes(nums: List[int]) -> None:
    i = 0
    j = 0

    while i < len(nums):
        if nums[i] == 0:
            i += 1
        else:
            if j < i:
                nums[j] = nums[i]
                nums[i] = 0
            i += 1
            j += 1


a = [0, 1, 0, 3, 12]
moveZeroes(a)
print(a)


def reverseString(s: List[str]) -> None:
    i = 0
    j = len(s) - 1
    while i < j:
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp
        i += 1
        j -= 1


b = ["h", "e", "l", "l", "o"]
reverseString(b)
print(b)
