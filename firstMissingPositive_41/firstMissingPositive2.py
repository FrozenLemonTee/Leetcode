"""
41. 缺失的第一个正数

给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。



示例 1:

输入: [1,2,0]
输出: 3

示例 2:

输入: [3,4,-1,1]
输出: 2

示例 3:

输入: [7,8,9,11,12]
输出: 1



提示：

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
"""
from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    length = len(nums)
    for i in range(0, length):
        while 0 < nums[i] <= length and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(0, length):
        if nums[i] != i + 1:
            return i + 1
    return length + 1


if __name__ == "__main__":
    print(firstMissingPositive([]))  # 1
    print(firstMissingPositive([1, 2, 4, 0]))  # 3
    print(firstMissingPositive([3, 4, -1, 5]))  # 1
    print(firstMissingPositive([7, 8, 9, 13, 12]))  # 1
    print(firstMissingPositive([0, 1, 1, -3, 1, 5, 4]))  # 2
