"""
128. 最长连续序列

给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。


"""
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0
    nums.sort()
    result = dp = 0
    pre = nums[0] - 1
    for i in range(0, len(nums)):
        if nums[i] - pre == 1:
            dp += 1
        elif nums[i] - pre > 1:
            dp = 1
        result = max(result, dp)
        pre = nums[i]
    return max(result, dp)


if __name__ == "__main__":
    test1 = [0]
    print(longestConsecutive(test1))  # 1
    test2 = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(test2))  # 4
    test3 = []
    print(longestConsecutive(test3))  # 0
    test4 = [100, 4, 200, 1, 5, 2, 6, 8, 9, 7, 11, 13, 12, 11]
    print(longestConsecutive(test4))  # 6
    test5 = [1, 2, 0, 1]
    print(longestConsecutive(test5))  # 3
    test6 = [0, 0]
    print(longestConsecutive(test6))  # 1
