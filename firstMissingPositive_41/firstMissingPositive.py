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
    if nums:
        i = 0
        while i <= len(nums) - 1:
            while nums[i] <= 0:
                nums.pop(i)
                if i > len(nums) - 1:
                    break
            i += 1
        length = len(nums)
        for j in range(0, length):
            if abs(nums[j]) - 1 <= length - 1 and nums[abs(nums[j]) - 1] > 0:
                nums[abs(nums[j]) - 1] *= -1
        for i in range(0, length):
            if nums[i] > 0:
                return i + 1
        return length + 1
    return 1


if __name__ == "__main__":
    print(firstMissingPositive([]))  # None
    print(firstMissingPositive([1, 2, 0]))  # 3
    print(firstMissingPositive([3, 4, -1, 1]))  # 2
    print(firstMissingPositive([7, 8, 9, 11, 12]))  # 1
    print(firstMissingPositive([0, 1, 1, -3, 2, 5, 4]))  # 3
